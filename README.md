# Svelte SPA + FastAPI Tutorial

A simple todo app demonstrating how to build a full-stack application with:
- **Backend**: FastAPI (Python) with Pydantic models
- **Frontend**: SvelteKit SPA with TypeScript
- **Type Safety**: Auto-generated TypeScript API client using Orval

This code accompanies the blog post: [Svelte SPA and FastAPI Integration Tutorial](https://turtledev.io/blog/svelte-spa-fastapi-integration-tutorial)

## Project Structure

```
svelte-spa-fastapi-tutorial/
├── backend/          # FastAPI Python backend
│   ├── main.py       # FastAPI app with CRUD endpoints
│   ├── models.py     # Pydantic models for Todo
│   └── requirements.txt
│
└── frontend/         # SvelteKit SPA
    ├── src/
    │   ├── routes/   # Pages
    │   └── lib/      # API client & components
    ├── orval.config.cjs  # Orval configuration for API client generation
    └── package.json
```

## Backend Setup

### Prerequisites
- Python 3.11+

### Installation
```bash
cd backend
pip install -r requirements.txt
```

### Running the backend
```bash
uvicorn main:app --reload
```

- API runs at `http://localhost:8000`
- API docs at `http://localhost:8000/docs`

## Frontend Setup

### Prerequisites
- Node.js 18+

### Installation
```bash
cd frontend
npm install
```

### Generate API Client
With the backend running, generate the TypeScript API client:
```bash
npm run generate
```

This creates typed API functions from the backend's OpenAPI spec.

### Running the frontend
```bash
npm run dev
```

Frontend runs at `http://localhost:5173`

## Development Workflow

1. Make changes to backend models or endpoints
2. Restart backend server
3. Run `npm run generate` in frontend to update API client
4. TypeScript will show errors if frontend needs updates
5. Update frontend code to match new API

## Key Features

- **Type Safety**: Backend Pydantic models → OpenAPI spec → TypeScript types
- **Auto-generated Client**: Changes in backend automatically flow to frontend
- **Simple Architecture**: Clear separation between frontend and backend
- **Local Development**: CORS configured, both services run locally

## Important Notes

- This is a tutorial/demo project - not production-ready
- Uses in-memory storage (data is lost on restart)
- No authentication or authorization
- CORS is wide open for local development
- For production use, check out [FastSvelte](https://fastsvelte.dev/)

## Learn More

Read the full tutorial: [Svelte SPA and FastAPI Integration Tutorial](https://turtledev.io/blog/svelte-spa-fastapi-integration-tutorial)
