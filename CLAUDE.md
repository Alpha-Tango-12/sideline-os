# CLAUDE.md - Sideline OS

## What is Sideline OS?
A shared weekly game-planning system for a football coaching staff — organizes the repeating weekly cycle (self-scout → install → practice scripting → final prep → game) that every structured program already runs. Full spec: `../../App Builder/SidelineOS.md`.

This is a **production-track project** — treat it as something that will eventually carry live coaching-staff data, not a throwaway prototype. That means: no secrets in code, Alembic migrations for every schema change (never `Base.metadata.create_all` outside tests), and CORS/auth scoped deliberately rather than left wide open "for now."

## Tech Stack
- **Web (`web/`):** React 19 + TypeScript + Vite 6 + Tailwind CSS v4
- **State:** Zustand 5 (UI state, e.g. active role) + TanStack Query 5 (server state)
- **Routing:** React Router DOM 7
- **Icons:** Lucide React
- **API (`api/`):** FastAPI (async) + SQLAlchemy 2.0 (async) + Alembic + Pydantic v2
- **DB:** SQLite (dev) → PostgreSQL (prod, via `asyncpg`)
- **Deployment:** Docker Compose (`docker-compose.yml` at repo root) + GitHub Actions CI (`.github/workflows/ci.yml`)

## Build Commands

```bash
# Backend
cd api
source .venv/bin/activate       # venv already created with python3.12
alembic upgrade head            # apply migrations
python run.py                   # http://localhost:8000
pytest                          # run tests

# Frontend
cd web
npm run dev                     # http://localhost:5173 (proxies /api → :8000)
npm run lint && npm run build && npm run test

# Full stack
docker compose up --build       # requires .env with POSTGRES_PASSWORD, SECRET_KEY
```

Use **`python3.12`**, not the system default — pydantic-core/asyncpg don't yet ship prebuilt wheels for newer CPython and will fail to build from source without Xcode's full toolchain.

## Architecture

```
routers/ (HTTP only, thin)
  → services/ (business logic, framework-agnostic, testable without HTTP/DB)
  → repositories/ (data access, isolates SQL)
  → models/ (SQLAlchemy ORM)
```

Frontend:
```
types/ → stores/ (Zustand) → services/ (typed API client) → pages/ → components/
```
- `stores/useRoleStore.ts` holds the active role + "view all roles" toggle — every page/dashboard should default to role-scoped data and read from this store
- `stores/useGamePlanStore.ts` holds the active `GamePlan`
- Components should go through `services/apiClient.ts`, not call `fetch` directly

## MVP Build Order (from spec — build in this sequence)

1. **Modular Workflow Manager** — weekly task board — **implemented**: `GET/POST /api/v1/tasks`, `PATCH /api/v1/tasks/{id}`, `GET /api/v1/gameplans/{id}/tasks`, `POST /api/v1/gameplans/{id}/tasks/apply-template`
2. **Sideline Sheet Builder** — down-and-distance play-call board — routes stubbed in `routers/sideline_sheets.py` (501s), build `SidelineSheetService` next
3. **Video & Annotation Hub** — tagged clip library — routes stubbed in `routers/video.py`. MVP scope is `source: external_url` only (Hudl-style links) — no self-hosted upload/transcoding pipeline until that's revisited
4. **Script & Card Automation** — generates from #2, depends on it existing — stubbed in `routers/scripts_cards.py`
5. **Sync Mechanism** — push to player PWA — stubbed in `routers/sync.py`, most infrastructure-heavy piece, build last

Each stub router has a `TODO(...)` comment naming the service to build and its priority — check there before starting the next feature.

## Data Model
Full entity list in the spec under "Data Model" — `api/app/models/` mirrors it 1:1 (`core.py`, `playbook.py`, `video.py`, `sideline_sheet.py`, `scripts.py`, `sync.py`, shared `enums.py`). Any schema change goes through `alembic revision --autogenerate -m "..."` — never hand-edit the DB or use `create_all` outside `tests/`.

## Design Language (from Claude Design prompts in the spec)
- Dark mode default, tablet-first (coaches run this off a Surface/iPad on the sideline)
- Base `#0B0F0D`, surfaces `#151B18`/`#1E2620`, borders `#33403A`, text `#F3F5F3`/`#8A9C90`
- Accent (turf green) `#2F7D46`, priority (chalk gold) `#E8B93D`, alert `#D64545`
- Never use color alone to convey status — always pair with an icon or label
- Touch targets ≥44–48px, no hover-only affordances — see spec's Coach Dashboard prompt for the full rationale

## Conventions
- Conventional commits: `feat(web): ...`, `feat(api): ...`, `fix(api): ...`
- TypeScript: strict mode, no `any` on exports
- Python: type hints on all signatures, async I/O by default, Pydantic for all request/response shapes
- Role is a first-class dimension — any new dashboard/query should default to "my role" scoping, not full-plan
