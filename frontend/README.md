# ULTRON AI — Frontend

The web interface for ULTRON AI, built with **Vue 3**, **TypeScript**, and **Vite**.

## Tech Stack

- **Vue 3** — Composition API with `<script setup>`
- **TypeScript** — Full type safety
- **Vite** — Fast dev server with HMR
- **Tailwind CSS** — Utility-first styling
- **NoVNC** — Real-time browser viewing from sandbox

## Project Structure

```
src/
├── components/        # Reusable UI components
│   ├── chat/          # Chat interface components
│   ├── sandbox/       # Browser viewer, file explorer
│   └── common/        # Shared components
│
├── pages/             # Route page views
├── api/               # Backend API client
├── composables/       # Vue composables (hooks)
├── constants/         # App-wide constants
├── locales/           # i18n translation files
├── lib/               # Utility libraries
└── assets/            # Static assets (CSS, images)
```

## Development

```bash
# Install dependencies
npm install

# Start dev server (http://localhost:5173)
npm run dev

# Build for production
npm run build

# Type check
npx vue-tsc --noEmit
```

## Features

- Real-time chat with streaming responses via SSE
- Live browser viewing via NoVNC WebSocket
- File explorer and editor for sandbox files
- Session management and sharing
- Multi-language support (i18n)
- Responsive design for desktop browsers
