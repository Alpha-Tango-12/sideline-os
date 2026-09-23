import uuid

from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["sync"])

# TODO(Sync Mechanism — MVP priority #5, most infrastructure-heavy): implement SyncService.
# PWA polls /sync-status and only pulls full payloads on a version bump — see spec's
# Sync Mechanism section for why a persistent WebSocket push is deliberately avoided.


@router.get("/gameplans/{game_plan_id}/sync-status", status_code=501)
async def get_sync_status(game_plan_id: uuid.UUID):
    raise HTTPException(status_code=501, detail="Sync Mechanism not yet implemented")


@router.post("/gameplans/{game_plan_id}/push", status_code=501)
async def push_to_devices(game_plan_id: uuid.UUID):
    raise HTTPException(status_code=501, detail="Sync Mechanism not yet implemented")


@router.post("/sync/ack", status_code=501)
async def device_ack():
    raise HTTPException(status_code=501, detail="Sync Mechanism not yet implemented")
