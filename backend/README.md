# ULTRON AI — Backend

The backend service for ULTRON AI, built with **FastAPI** and **Python 3.12** using Domain-Driven Design (DDD) architecture.

## Architecture

```
app/
├── domain/            # Core business logic
│   ├── models/        # Domain entities and value objects
│   └── services/
│       ├── agents/    # AI agents (base, execution)
│       ├── flows/     # Orchestration (PlanAct flow)
│       └── tools/     # Tool implementations (browser, shell, file, search)
│
├── infrastructure/    # External service integrations
│   └── external/
│       ├── llm/       # LLM clients (OpenAI-compatible)
│       ├── search/    # Search providers (Bing, Google, Baidu)
│       └── storage/   # File storage adapters
│
├── interfaces/        # API layer
│   ├── api/           # REST routes
│   └── ws/            # WebSocket handlers
│
├── application/       # Application services
│   ├── services/      # Use cases
│   └── errors/        # Error handling
│
├── core/              # Configuration and utilities
└── main.py            # Application entrypoint
```

## Key Components

### PlanAct Agent
The core intelligence loop that decomposes user tasks into executable steps. Uses LLM function-calling to select tools and iterate until the task is complete.

### Tool System
- **BrowserTool** — Controls headless Chrome via CDP (Chrome DevTools Protocol)
- **ShellTool** — Executes shell commands in the sandbox
- **FileTool** — File CRUD operations in the sandbox
- **SearchTool** — Web search via configured provider
- **MCPTool** — Dynamic tools loaded from MCP servers

### LLM Integration
Supports any OpenAI-compatible API. The `openai_llm.py` client handles streaming, function calling, and response format negotiation.

## Running Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Tests

```bash
pip install -r tests/requirements.txt
pytest
```

## Environment Variables

See the root [README.md](../README.md#-configuration) for all configuration options.
