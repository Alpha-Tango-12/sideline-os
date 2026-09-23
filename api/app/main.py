from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.routers import gameplans, playbook, scripts_cards, sideline_sheets, sync, tasks, video

settings = get_settings()

if settings.is_production and settings.secret_key.startswith("dev-only"):
    raise RuntimeError("SECRET_KEY must be set via environment in production")

app = FastAPI(title="Sideline OS API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_PREFIX = "/api/v1"
app.include_router(gameplans.router, prefix=API_PREFIX)
app.include_router(tasks.router, prefix=API_PREFIX)
app.include_router(playbook.router, prefix=API_PREFIX)
app.include_router(video.router, prefix=API_PREFIX)
app.include_router(sideline_sheets.router, prefix=API_PREFIX)
app.include_router(scripts_cards.router, prefix=API_PREFIX)
app.include_router(sync.router, prefix=API_PREFIX)


@app.get("/health")
async def health():
    return {"status": "ok", "environment": settings.environment}
