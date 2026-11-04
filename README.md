# RolangMalang League HUD

A real-time OBS broadcasting overlay system for our community's League of Legends amateur tournament, "RolangMalang League."

## Features
- **Tournament API Integration**: Automatically receives live match data (kills, gold, objectives) via webhooks.
- **OBS Browser Source**: Renders a professional esports HUD dynamically using `hud.html`.

## Project Structure
- `hud.html`: Frontend overlay UI for OBS.
- `server.py`: Backend server handling webhook/websocket data communication.
