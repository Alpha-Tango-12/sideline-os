import uuid

from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["script-card-automation"])

# TODO(Script & Card Automation — MVP priority #4): implement ScriptCardGenService.
# Depends on the Sideline Sheet Builder existing, per the spec's build sequencing.


@router.post("/practice-scripts/generate", status_code=501)
async def generate_practice_script():
    raise HTTPException(status_code=501, detail="Script & Card Automation not yet implemented")


@router.get("/practice-scripts/{script_id}")
async def get_practice_script(script_id: uuid.UUID):
    raise HTTPException(status_code=501, detail="Script & Card Automation not yet implemented")


@router.post("/scout-cards/generate", status_code=501)
async def generate_scout_card():
    raise HTTPException(status_code=501, detail="Script & Card Automation not yet implemented")


@router.get("/scout-cards/{card_id}")
async def get_scout_card(card_id: uuid.UUID):
    raise HTTPException(status_code=501, detail="Script & Card Automation not yet implemented")
