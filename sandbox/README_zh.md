# ULTRON AI — 沙箱

ULTRON AI 的安全执行环境。每个任务都在隔离的 Docker 容器中运行，包含完整的 Ubuntu 环境、无头 Chrome 浏览器和工具 API。

## 包含内容

- **Ubuntu 22.04** 基础镜像
- **Chrome** 无头浏览器 + VNC 访问
- **xvfb + x11vnc + websockify** — 通过 WebSocket 实时查看浏览器
- **FastAPI 服务器** — 暴露文件、终端和浏览器工具 API
- **Supervisord** — 进程管理器

## 工作原理

1. 后端通过 Docker API 创建新的沙箱容器
2. Supervisord 启动 Chrome、VNC、websockify 和 API 服务器
3. 后端通过 REST API 与沙箱工具通信
4. 前端通过 NoVNC WebSocket 连接浏览器视图
5. 容器在 `SANDBOX_TTL_MINUTES` 后自动销毁

## 测试

```bash
pip install -r tests/requirements.txt
pytest
```
