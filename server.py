from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn
import json
import asyncio

app = FastAPI()

# OBS 브라우저 소스(HUD) 연결 클라이언트 관리
connected_clients = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    print("OBS HUD 연결됨")
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print("OBS HUD 연결 해제됨")

@app.post("/riot-webhook")
async def riot_webhook(event: dict):
    """
    라이엇 토너먼트 API 서버가 경기 이벤트를 쏘아주는 웹훅 엔드포인트
    """
    print("라이엇 웹훅 데이터 수신:", event)
    
    # 라이엇 페이로드 구조에 맞춰 데이터 파싱 (기본값 설정)
    payload = {
        "status": "active",
        "gameTime": event.get("gameTime", "00:00"),
        "blueKills": event.get("blueKills", 0),
        "redKills": event.get("redKills", 0),
        "blueGold": event.get("blueGold", "0.0k"),
        "redGold": event.get("redGold", "0.0k"),
        "blueTurrets": event.get("blueTurrets", 0),
        "blueBarons": event.get("blueBarons", 0),
        "blueDragons": event.get("blueDragons", 0),
        "blueHordes": event.get("blueHordes", 0),
        "redTurrets": event.get("redTurrets", 0),
        "redBarons": event.get("redBarons", 0),
        "redDragons": event.get("redDragons", 0),
        "redHordes": event.get("redHordes", 0),
    }

    # 연결된 모든 OBS HUD에 실시간 브로드캐스트
    if connected_clients:
        message = json.dumps(payload)
        await asyncio.gather(*[client.send_text(message) for client in connected_clients])

    return {"status": "success"}, 200

if __name__ == "__main__":
    # 포트 8765에서 HTTP와 WebSocket 동시 구동
    uvicorn.run(app, host="0.0.0.0", port=8765)