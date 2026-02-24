# ULTRON AI — 前端

ULTRON AI 的 Web 界面，基于 **Vue 3**、**TypeScript** 和 **Vite** 构建。

## 技术栈

- **Vue 3** — Composition API + `<script setup>`
- **TypeScript** — 完整类型安全
- **Vite** — 快速开发服务器和 HMR
- **Tailwind CSS** — 原子化 CSS
- **NoVNC** — 实时浏览器查看

## 开发

```bash
# 安装依赖
npm install

# 启动开发服务器 (http://localhost:5173)
npm run dev

# 生产构建
npm run build
```

## 功能

- 通过 SSE 实现实时流式聊天
- 通过 NoVNC WebSocket 实时查看浏览器
- 沙箱文件资源管理器和编辑器
- 会话管理和分享
- 多语言支持（i18n）
