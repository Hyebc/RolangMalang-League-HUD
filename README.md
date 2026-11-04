# RolangMalang League HUD

A professional real-time broadcasting HUD system designed for our community's amateur League of Legends tournament, **"RolangMalang League."**

## Overview
This project replaces unstable screen-capture OCR methods with official **Riot Tournament API** integration. It receives live match events via webhooks and dynamically renders clean esports overlays on OBS (Open Broadcaster Software).

## Architecture
1. **Backend (`server.py`)**: Built with FastAPI. Listens for incoming webhook events from Riot Tournament servers and broadcasts data via WebSockets.
2. **Frontend (`hud.html`)**: A lightweight HTML/CSS browser source overlay optimized for OBS, featuring responsive typography and vector SVG icons.

## Tech Stack
- Python (FastAPI, Uvicorn, WebSockets)
- HTML5 / CSS3 / JavaScript (OBS Browser Source)
- Riot Games Tournament API (Webhook integration)
