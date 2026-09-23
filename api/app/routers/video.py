import uuid

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/clips", tags=["video-hub"])

# TODO(Video & Annotation Hub — MVP priority #3): implement VideoService.
# MVP scopes VideoClip.source to external_url first (e.g. Hudl links) —
# self-hosted upload/transcoding is deferred per the Open Questions in the spec.


@router.get("")
async def list_clips(tag: str | None = None, formation_id: uuid.UUID | None = None, situation: str | None = None):
    raise HTTPException(status_code=501, detail="Video & Annotation Hub not yet implemented")


@router.post("", status_code=501)
async def register_clip():
    raise HTTPException(status_code=501, detail="Video & Annotation Hub not yet implemented")


@router.post("/{clip_id}/annotations", status_code=501)
async def add_annotation(clip_id: uuid.UUID):
    raise HTTPException(status_code=501, detail="Video & Annotation Hub not yet implemented")


@router.post("/{clip_id}/tags", status_code=501)
async def tag_clip(clip_id: uuid.UUID):
    raise HTTPException(status_code=501, detail="Video & Annotation Hub not yet implemented")


@router.post("/{clip_id}/link-play", status_code=501)
async def link_clip_to_play(clip_id: uuid.UUID):
    raise HTTPException(status_code=501, detail="Video & Annotation Hub not yet implemented")
