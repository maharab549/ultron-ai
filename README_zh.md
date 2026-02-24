<p align="center">
  <h1 align="center">⚡ ULTRON AI</h1>
  <p align="center"><strong>开源自主 AI 智能体平台</strong></p>
  <p align="center">由 <a href="https://github.com/maharab549">Maharab Hossen</a> 构建</p>
</p>

<p align="center">
  <a href="https://github.com/maharab549/ai-manus/stargazers"><img src="https://img.shields.io/github/stars/maharab549/ai-manus?style=for-the-badge&color=gold" alt="Stars"></a>
  <a href="https://github.com/maharab549/ai-manus/network/members"><img src="https://img.shields.io/github/forks/maharab549/ai-manus?style=for-the-badge&color=blue" alt="Forks"></a>
  <a href="https://github.com/maharab549/ai-manus/issues"><img src="https://img.shields.io/github/issues/maharab549/ai-manus?style=for-the-badge&color=red" alt="Issues"></a>
</p>

<p align="center">
  <a href="#-快速开始">快速开始</a> •
  <a href="#-功能特性">功能特性</a> •
  <a href="#-系统架构">系统架构</a> •
  <a href="#-配置说明">配置说明</a> •
  <a href="./README.md">English</a>
</p>

---

## 🤔 什么是 ULTRON AI？

**ULTRON AI** 是一个开源的通用 AI 智能体系统，能够自主规划、推理和执行复杂任务。给它一个目标，它会自动分解任务、使用工具、浏览网络、编写代码、操作文件，并在安全的沙箱环境中交付结果。

可以将它看作 Manus AI、ChatGPT Code Interpreter 或 Devin 的自托管替代方案 — 完全开源，由你掌控。

### 对比

| 功能 | ULTRON AI | Manus AI | ChatGPT |
|:---|:---:|:---:|:---:|
| 开源 | ✅ | ❌ | ❌ |
| 自托管 | ✅ | ❌ | ❌ |
| 网页浏览 | ✅ | ✅ | ✅ |
| 代码执行 | ✅ | ✅ | ✅ |
| 文件操作 | ✅ | ✅ | ✅ |
| 沙箱环境 | ✅ | ✅ | ❌ |
| MCP 工具集成 | ✅ | ❌ | ❌ |
| 自定义 LLM | ✅ | ❌ | ❌ |
| 本地/离线模式 | ✅ | ❌ | ❌ |
| 免费使用 | ✅ | ❌ | ❌ |

---

## ✨ 功能特性

- 🧠 **自主规划** — 使用 Plan-Act 架构将复杂任务分解为可执行的步骤
- 🌐 **实时浏览器** — 在沙箱中运行完整的 Chrome 浏览器，通过 NoVNC 实时查看
- 💻 **Shell 和代码执行** — 在隔离的 Ubuntu 容器中运行 bash 命令和 Python 脚本
- 📁 **文件管理** — 在沙箱文件系统中创建、读取、编辑和管理文件
- 🔌 **MCP 工具生态** — 通过 MCP 服务器扩展功能（GitHub、数据库、API 等）
- 🔍 **网页搜索** — 集成 Bing、Google 或百度搜索
- 🔐 **安全沙箱** — 每个任务在独立的 Docker 容器中运行，自动清理
- 👥 **多用户认证** — 内置邮箱/密码、本地管理员或无认证模式
- 🎨 **现代化 UI** — Vue 3 界面，支持实时流、会话分享和工具可视化
- 🤖 **任何 LLM** — 支持 OpenAI、DeepSeek、LM Studio、Ollama 或任何 OpenAI 兼容 API

---

## 🚀 快速开始

### 环境要求

- **Docker Desktop** (Windows/Mac) 或 **Docker Engine** (Linux) — v20.10+
- 支持 **函数调用** 的 LLM（OpenAI、DeepSeek、LM Studio 等）

### 1. 克隆与配置

```bash
git clone https://github.com/maharab549/ai-manus.git
cd ai-manus
cp docker-compose-example.yml docker-compose.yml
```

编辑 `docker-compose.yml`，设置你的 LLM 提供商：

**OpenAI：**
```yaml
- API_BASE=https://api.openai.com/v1
- API_KEY=sk-your-key-here
- MODEL_NAME=gpt-4o
```

**DeepSeek：**
```yaml
- API_BASE=https://api.deepseek.com/v1
- API_KEY=sk-your-key-here
- MODEL_NAME=deepseek-chat
```

**LM Studio（本地）：**
```yaml
- API_BASE=http://host.docker.internal:1234/v1
- API_KEY=lm-studio
- MODEL_NAME=your-model-name
```

### 2. 启动

```bash
docker compose up -d
```

### 3. 访问

在浏览器中打开 **http://localhost:5173**。

> **提示：** 看到 `sandbox-1 exited with code 0` 是正常的，它只是预拉取沙箱镜像。

---

## ⚙️ 系统架构

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   前端       │────▶│    后端       │────▶│     沙箱         │
│  (Vue 3)    │◀────│  (FastAPI)   │◀────│ (Ubuntu+Chrome) │
└─────────────┘ SSE └──────────────┘     └─────────────────┘
                          │                       │
                     ┌────┴────┐            ┌─────┴─────┐
                     │ MongoDB │            │  浏览器    │
                     │  Redis  │            │  终端      │
                     └─────────┘            │  文件      │
                                            └───────────┘
```

---

## 📋 配置说明

| 变量 | 说明 | 默认值 |
|:---|:---|:---|
| `API_BASE` | LLM API 地址 | `http://mockserver:8090/v1` |
| `API_KEY` | LLM API 密钥 | — |
| `MODEL_NAME` | 模型标识符 | `deepseek-chat` |
| `SEARCH_PROVIDER` | 搜索引擎（`bing`、`google`、`baidu`） | `baidu` |
| `AUTH_PROVIDER` | 认证模式（`password`、`local`、`none`） | `password` |

完整配置文档请参阅 [配置说明](docs/configuration.md)。

---

## 📜 开源协议

本项目开源。详情请查看 [LICENSE](LICENSE) 文件。

---

<p align="center">
  <strong>⭐ 如果你觉得 ULTRON AI 有用，请给个 Star！</strong><br>
  <a href="https://github.com/maharab549/ai-manus">https://github.com/maharab549/ai-manus</a>
</p>
