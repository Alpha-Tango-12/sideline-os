import uuid

from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["sideline-sheet"])

# TODO(Sideline Sheet Builder — MVP priority #2): implement SidelineSheetService
# backing these routes once the Workflow Manager (priority #1) is validated.


@router.get("/gameplans/{game_plan_id}/sideline-sheet")
async def get_current_sideline_sheet(game_plan_id: uuid.UUID):
    raise HTTPException(status_code=501, detail="Sideline Sheet Builder not yet implemented")


@router.post("/sideline-sheets/{sheet_id}/entries", status_code=501)
async def add_sideline_sheet_entry(sheet_id: uuid.UUID):
    raise HTTPException(status_code=501, detail="Sideline Sheet Builder not yet implemented")


@router.patch("/sideline-sheets/{sheet_id}/entries/{entry_id}", status_code=501)
async def update_sideline_sheet_entry(sheet_id: uuid.UUID, entry_id: uuid.UUID):
    raise HTTPException(status_code=501, detail="Sideline Sheet Builder not yet implemented")


@router.post("/sideline-sheets/{sheet_id}/finalize", status_code=501)
async def finalize_sideline_sheet(sheet_id: uuid.UUID):
    raise HTTPException(status_code=501, detail="Sideline Sheet Builder not yet implemented")
