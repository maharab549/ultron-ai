# ULTRON AI — Local Development Setup Guide

This guide walks you through setting up ULTRON AI for local development with hot-reload support.

## Prerequisites

| Tool | Version | Purpose |
|:---|:---|:---|
| Docker Desktop / Engine | 20.10+ | Container runtime |
| Docker Compose | v2+ | Service orchestration |
| Node.js | 18+ | Frontend development |
| Python | 3.12+ | Backend development |
| Git | Latest | Version control |

## Step 1: Clone the Repository

```bash
git clone https://github.com/maharab549/ultron-ai.git
cd ai-manus
```

## Step 2: Environment Configuration

Copy the environment template and configure your LLM settings:

```bash
cp .env.example .env
```

Open `.env` and set these variables:

```env
# LLM Configuration
API_KEY=your-api-key
API_BASE=https://api.openai.com/v1
MODEL_NAME=gpt-4o

# Or for local LM Studio:
# API_KEY=lm-studio
# API_BASE=http://host.docker.internal:1234/v1
# MODEL_NAME=your-model-name
```

## Step 3: Start Development Services

The project includes a development compose file that mounts source code for hot-reload:

```bash
# Start all services in development mode
./dev.sh up -d

# Check service status
./dev.sh ps
```

This starts:
- **Frontend** on `http://localhost:5173` (Vite dev server with HMR)
- **Backend** on port 8000 (FastAPI with auto-reload)
- **MongoDB** on port 27017
- **Redis** on port 6379
- **Mock Server** on port 8090 (for testing without a real LLM)

## Step 4: View Logs

```bash
# All services
./dev.sh logs -f

# Specific service
./dev.sh logs -f backend
./dev.sh logs -f frontend
./dev.sh logs -f sandbox
```

## Step 5: Access the App

Open **http://localhost:5173** in your browser.

Default local auth credentials (when `AUTH_PROVIDER=local`):
- Email: `admin@example.com`
- Password: `admin`

## Project Structure

```
ultron-ai/
├── frontend/              # Vue 3 + TypeScript + Vite
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page views
│   │   ├── api/           # API client layer
│   │   ├── composables/   # Vue composables (hooks)
│   │   └── locales/       # i18n translations
│   └── vite.config.ts
│
├── backend/               # FastAPI + Python 3.12
│   └── app/
│       ├── domain/        # Business logic
│       │   ├── services/  # Agents, flows, tools
│       │   └── models/    # Domain models
│       ├── infrastructure/# External integrations
│       │   └── external/  # LLM clients, search, storage
│       ├── interfaces/    # HTTP routes, WebSocket
│       └── application/   # Application services
│
├── sandbox/               # Docker sandbox image
│   └── app/               # Sandbox API server
│       ├── services/      # File, shell, browser services
│       └── api/           # REST API routes
│
├── mockserver/            # Mock LLM for development
└── docs/                  # Docsify documentation
```

## Running Tests

```bash
# Backend tests
cd backend
pip install -r tests/requirements.txt
pytest

# Sandbox tests
cd sandbox
pip install -r tests/requirements.txt
pytest
```

## MCP Configuration (Optional)

To use MCP tools like GitHub API:

1. Copy the MCP config template:
   ```bash
   cp mcp.json.example mcp.json
   ```

2. Edit `mcp.json` with your tokens:
   ```json
   {
     "mcpServers": {
       "github": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-github"],
         "transport": "stdio",
         "enabled": true,
         "env": {
           "GITHUB_TOKEN": "your-github-token"
         }
       }
     }
   }
   ```

3. Uncomment the MCP volume mount in `docker-compose.yml`:
   ```yaml
   volumes:
     - ./mcp.json:/etc/mcp.json
   ```

## Troubleshooting

### Container can't connect to local LLM (LM Studio / Ollama)

Use `host.docker.internal` instead of `localhost` or `127.0.0.1`:
```env
API_BASE=http://host.docker.internal:1234/v1
```

### Sandbox containers not cleaning up

Sandboxes auto-expire after `SANDBOX_TTL_MINUTES` (default: 30). To manually remove:
```bash
docker ps -a | grep sandbox | awk '{print $1}' | xargs docker rm -f
```

### Frontend not loading

Check if the backend is running:
```bash
./dev.sh logs -f backend
```

### Docker build fails (network issues)

If Docker can't pull base images, use the volume mount workaround to inject code changes:
```yaml
# In docker-compose.yml, under backend service:
volumes:
  - ./backend/app:/app/app:ro
```
