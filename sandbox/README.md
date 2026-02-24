# ULTRON AI — Sandbox

The secure execution environment for ULTRON AI. Each task runs inside an isolated Docker container with a full Ubuntu environment, headless Chrome browser, and tool APIs.

## What's Inside

- **Ubuntu 22.04** base image
- **Chrome** headless browser with VNC access
- **xvfb + x11vnc + websockify** — Enables real-time browser viewing via WebSocket
- **FastAPI server** — Exposes file, shell, and browser tool APIs
- **Supervisord** — Process manager for all sandbox services

## Architecture

```
sandbox/
├── app/
│   ├── api/           # REST API routes
│   │   └── v1/        # API version 1
│   ├── services/      # Service implementations
│   │   ├── file/      # File operations
│   │   ├── shell/     # Command execution
│   │   └── browser/   # Chrome control
│   ├── models/        # Data models
│   ├── schemas/       # Request/response schemas
│   └── core/          # Configuration
│
├── resource/          # Test resources
├── supervisord.conf   # Process manager config
└── Dockerfile         # Container image definition
```

## How It Works

1. Backend creates a new sandbox container via Docker API
2. Supervisord starts Chrome, VNC, websockify, and the API server
3. Backend communicates with sandbox tools via REST API
4. Frontend connects to the browser view via NoVNC WebSocket
5. Container auto-destroys after `SANDBOX_TTL_MINUTES`

## API Endpoints

| Method | Path | Description |
|:---|:---|:---|
| POST | `/api/v1/shell/exec` | Execute shell command |
| GET | `/api/v1/files/` | List files |
| POST | `/api/v1/files/upload` | Upload file |
| GET | `/api/v1/files/download` | Download file |

## Tests

```bash
pip install -r tests/requirements.txt
pytest
```
