<p align="center">
  <h1 align="center">⚡ ULTRON AI</h1>
  <p align="center"><strong>Open-Source Autonomous AI Agent Platform</strong></p>
  <p align="center">Built by <a href="https://github.com/maharab549">Maharab Hossen</a></p>
</p>

<p align="center">
  <a href="https://github.com/maharab549/ai-manus/stargazers"><img src="https://img.shields.io/github/stars/maharab549/ai-manus?style=for-the-badge&color=gold" alt="Stars"></a>
  <a href="https://github.com/maharab549/ai-manus/network/members"><img src="https://img.shields.io/github/forks/maharab549/ai-manus?style=for-the-badge&color=blue" alt="Forks"></a>
  <a href="https://github.com/maharab549/ai-manus/issues"><img src="https://img.shields.io/github/issues/maharab549/ai-manus?style=for-the-badge&color=red" alt="Issues"></a>
  <a href="https://github.com/maharab549/ai-manus/blob/main/LICENSE"><img src="https://img.shields.io/github/license/maharab549/ai-manus?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-configuration">Configuration</a> •
  <a href="./README_zh.md">中文文档</a>
</p>

---

## 🤔 What is ULTRON AI?

**ULTRON AI** is an open-source, general-purpose AI agent system that can autonomously plan, reason and execute complex tasks. Give it a goal and it will break it down, use tools, browse the web, write code, manipulate files, and deliver results — all inside a secure sandboxed environment.

Think of it as your own self-hosted alternative to Manus AI, ChatGPT with Code Interpreter, or Devin — but fully open source and under your control.

### How ULTRON AI Compares

| Capability | ULTRON AI | Manus AI | ChatGPT |
|:---|:---:|:---:|:---:|
| Open Source | ✅ | ❌ | ❌ |
| Self-Hosted | ✅ | ❌ | ❌ |
| Web Browsing | ✅ | ✅ | ✅ |
| Code Execution | ✅ | ✅ | ✅ |
| File Operations | ✅ | ✅ | ✅ |
| Sandboxed Environment | ✅ | ✅ | ❌ |
| MCP Tool Integration | ✅ | ❌ | ❌ |
| Custom LLM Backend | ✅ | ❌ | ❌ |
| Local / Offline Mode | ✅ | ❌ | ❌ |
| Free to Use | ✅ | ❌ | ❌ |

---

## ✨ Features

- 🧠 **Autonomous Planning** — Breaks complex tasks into actionable steps using Plan-Act architecture
- 🌐 **Live Web Browser** — Full Chrome browser running inside the sandbox, viewable via NoVNC in real-time
- 💻 **Shell & Code Execution** — Runs bash commands, Python scripts, and more inside an isolated Ubuntu container
- 📁 **File Management** — Creates, reads, edits, and organizes files within the sandbox filesystem
- 🔌 **MCP Tool Ecosystem** — Extend capabilities with Model Context Protocol servers (GitHub, databases, APIs, etc.)
- 🔍 **Web Search** — Integrated search via Bing, Google, or Baidu
- 🔐 **Secure Sandbox** — Every task runs in a disposable Docker container with automatic cleanup
- 👥 **Multi-User Auth** — Built-in authentication with email/password, local admin, or no-auth modes
- 🎨 **Modern Web UI** — Clean Vue 3 interface with real-time streaming, session sharing, and tool visualization
- 🤖 **Any LLM** — Works with OpenAI, DeepSeek, LM Studio, Ollama, or any OpenAI-compatible API

---

## 🚀 Quick Start

### Prerequisites

- **Docker Desktop** (Windows/Mac) or **Docker Engine** (Linux)  — v20.10+
- An LLM with **function calling** support (OpenAI, DeepSeek, LM Studio, etc.)

### 1. Clone & Configure

```bash
git clone https://github.com/maharab549/ai-manus.git
cd ai-manus
cp docker-compose-example.yml docker-compose.yml
```

Edit `docker-compose.yml` and set your LLM provider:

**OpenAI:**
```yaml
- API_BASE=https://api.openai.com/v1
- API_KEY=sk-your-key-here
- MODEL_NAME=gpt-4o
```

**DeepSeek:**
```yaml
- API_BASE=https://api.deepseek.com/v1
- API_KEY=sk-your-key-here
- MODEL_NAME=deepseek-chat
```

**LM Studio (Local):**
```yaml
- API_BASE=http://host.docker.internal:1234/v1
- API_KEY=lm-studio
- MODEL_NAME=your-model-name
```

**Ollama (Local):**
```yaml
- API_BASE=http://host.docker.internal:11434/v1
- API_KEY=ollama
- MODEL_NAME=llama3
```

### 2. Launch

```bash
docker compose up -d
```

### 3. Open

Visit **http://localhost:5173** in your browser. That's it!

> **Note:** You'll see `sandbox-1 exited with code 0` — this is expected. It pre-pulls the sandbox image.

---

## ⚙️ Architecture

ULTRON AI follows a clean, modular architecture:

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Frontend    │────▶│   Backend    │────▶│    Sandbox      │
│  (Vue 3)    │◀────│  (FastAPI)   │◀────│  (Ubuntu+Chrome)│
└─────────────┘ SSE └──────────────┘     └─────────────────┘
                          │                       │
                     ┌────┴────┐            ┌─────┴─────┐
                     │ MongoDB │            │  Browser   │
                     │  Redis  │            │  Shell     │
                     └─────────┘            │  Files     │
                                            └───────────┘
```

**How it works:**

1. User sends a task through the web interface
2. Backend creates a fresh Docker sandbox and routes the task to the **PlanAct Agent**
3. The agent decomposes the task into steps, calling tools (browser, shell, files, search, MCP) as needed
4. All progress streams back to the frontend via Server-Sent Events (SSE)
5. User can watch the browser in real-time via NoVNC and inspect all tool outputs

---

## 📋 Configuration

| Variable | Description | Default |
|:---|:---|:---|
| `API_BASE` | LLM API endpoint | `http://mockserver:8090/v1` |
| `API_KEY` | LLM API key | — |
| `MODEL_NAME` | Model identifier | `deepseek-chat` |
| `TEMPERATURE` | Response randomness (0-1) | `0.7` |
| `MAX_TOKENS` | Max response tokens | `2000` |
| `SEARCH_PROVIDER` | Search engine (`bing`, `google`, `baidu`) | `baidu` |
| `AUTH_PROVIDER` | Auth mode (`password`, `local`, `none`) | `password` |
| `MCP_CONFIG_PATH` | Path to MCP config file | `/etc/mcp.json` |
| `LOG_LEVEL` | Logging level | `INFO` |

See [full configuration docs](docs/en/configuration.md) for all options including MongoDB, Redis, JWT, email, and sandbox settings.

---

## 🛠️ Development

For local development with hot-reload:

```bash
# Clone
git clone https://github.com/maharab549/ai-manus.git
cd ai-manus

# Copy env template
cp .env.example .env
# Edit .env with your LLM settings

# Start all services
./dev.sh up -d

# View logs
./dev.sh logs -f backend
```

See [LOCAL_SETUP_GUIDE.md](LOCAL_SETUP_GUIDE.md) for detailed development setup instructions.

---

## 📁 Project Structure

```
ultron-ai/
├── frontend/          # Vue 3 + TypeScript web interface
├── backend/           # FastAPI Python backend (DDD architecture)
│   └── app/
│       ├── domain/        # Business logic, agents, flows
│       ├── infrastructure/# LLM clients, DB, external services
│       ├── interfaces/    # API routes, WebSocket handlers
│       └── application/   # Application services
├── sandbox/           # Ubuntu Docker sandbox with Chrome + tools
├── mockserver/        # Development mock LLM server
├── docs/              # Documentation site (Docsify)
└── docker-compose.yml # Production deployment
```

---

## 🗺️ Roadmap

- [x] Browser takeover with live viewing
- [x] MCP tool integration
- [x] Multi-user authentication
- [x] Session sharing
- [ ] Settings UI panel
- [ ] Timeline playback
- [ ] Deploy & Expose tools
- [ ] Docker Swarm support
- [ ] Windows & mobile optimization
- [ ] Enterprise sandbox security

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is open-source. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>⭐ Star this repo if you find ULTRON AI useful!</strong><br>
  <a href="https://github.com/maharab549/ai-manus">https://github.com/maharab549/ai-manus</a>
</p>
