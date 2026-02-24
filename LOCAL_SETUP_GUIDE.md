# Manus 1.6 Max Local Setup Guide

This guide will help you set up and run the Manus 1.6 Max project on your local machine.

## Prerequisites

- **Docker & Docker Compose**: Required for running the backend, database, and sandbox.
- **Node.js (v18+)**: Required for the frontend.
- **Python 3.11+**: Required for local backend development (optional if using Docker).

---

## Step 1: Clone and Prepare

1. Unzip the project files to your desired directory.
2. Navigate to the project root:
   ```bash
   cd ai-manus-main
   ```
3. Copy the environment template:
   ```bash
   cp .env.example .env
   ```

## Step 2: Configure Environment Variables

Open the `.env` file and configure your preferred LLM provider:

### For OpenAI / DeepSeek:
```env
LLM_PROVIDER=openai
API_KEY=your_openai_or_deepseek_key
API_BASE=https://api.openai.com/v1 # or your deepseek base
```

### For Google Gemini:
```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL_NAME=gemini-1.5-pro
```

### For Ollama (Local):
```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL_NAME=llama3
```

---

## Step 3: Start the Backend (Docker)

The easiest way to run the backend and its dependencies (MongoDB, Redis, Sandbox) is using Docker Compose:

```bash
docker-compose up -d
```

This will start:
- **Backend API**: Port 8000
- **MongoDB**: Port 27017
- **Redis**: Port 6379
- **Sandbox**: Isolated environment for tool execution

---

## Step 4: Start the Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   pnpm install # or npm install
   ```
3. Start the development server:
   ```bash
   pnpm dev
   ```
4. Open your browser and go to `http://localhost:5173`.

---

## Step 5: Verify Setup

1. Log in using the default credentials (if `AUTH_PROVIDER=local`):
   - **Email**: `admin@example.com`
   - **Password**: `admin`
2. Start a new chat and try a simple command like "Hello" or "Check the current directory" to verify the LLM and Sandbox are working.

---

## Troubleshooting

- **LLM Connection Issues**: Ensure your API keys are correct and you have internet access (for OpenAI/Gemini) or Ollama is running locally.
- **Docker Errors**: Make sure Docker Desktop is running and you have enough disk space.
- **Frontend Build Errors**: Ensure you are using Node.js v18 or higher.

For more detailed documentation, visit [docs.ai-manus.com](https://docs.ai-manus.com).
