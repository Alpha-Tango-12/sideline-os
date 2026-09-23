# Sideline OS

A shared weekly game-planning system for football coaching staffs — built around the structured weekly cycle every program already runs (self-scout → install → practice scripting → final prep → game).

Full spec: `../App Builder/SidelineOS.md`

## Stack

- **`web/`** — React + TypeScript + Vite + Tailwind CSS, Zustand + TanStack Query, React Router. Also ships as an installable PWA for the player-facing sync view.
- **`api/`** — FastAPI (async) + SQLAlchemy 2.0 + Alembic. SQLite for dev, PostgreSQL for prod.

## Local Development

### Backend

```bash
cd api
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
python run.py            # http://localhost:8000
```

### Frontend

```bash
cd web
npm install
cp .env.example .env
npm run dev               # http://localhost:5173, proxies /api to :8000
```

### Full stack (Docker Compose)

```bash
cp api/.env.example .env   # then set POSTGRES_PASSWORD and SECRET_KEY
docker compose up --build
```

## MVP Build Order

1. **Modular Workflow Manager** — weekly task board, role-scoped — implemented (`/api/v1/gameplans/{id}/tasks`, `/api/v1/tasks`)
2. **Sideline Sheet Builder** — down-and-distance play-call board — scaffolded, not implemented
3. **Video & Annotation Hub** — tagged clip library — scaffolded, not implemented
4. **Script & Card Automation** — generates from #2 — scaffolded, not implemented
5. **Sync Mechanism** — push to player devices — scaffolded, not implemented

See `api/app/routers/` for the full route contract — unimplemented routes return `501` with a `TODO` comment pointing at the responsible service.

## Testing

```bash
cd web && npm run lint && npm run build && npm run test
cd api && source .venv/bin/activate && pytest
```
