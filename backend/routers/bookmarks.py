from fastapi import APIRouter, HTTPException
from schemas.bookmark import BookmarkCreate, BookmarkUpdate, BookmarkResponse
from database import db, next_id
from datetime import datetime

router = APIRouter(prefix="/bookmarks", tags=["bookmarks"])


@router.get("/", response_model=list[BookmarkResponse])
def get_bookmarks():
    return list(db.values())


@router.post("/", response_model=BookmarkResponse, status_code=201)
def create_bookmark(bookmark: BookmarkCreate):
    id = next_id()
    db[id] = {
        "id": id,
        "name": bookmark.name,
        "url": str(bookmark.url),
        "tags": bookmark.tags,
        "created_at": datetime.now(),
    }
    return db[id]


@router.patch("/{id}", response_model=BookmarkResponse)
def update_bookmark(id: int, bookmark: BookmarkUpdate):
    updates = bookmark.model_dump(exclude_unset=True)
    if id not in db:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    db[id].update(updates)
    return db[id]


@router.delete("/{id}", status_code=204)
def delete_bookmark(id: int):
    if id not in db:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    db.pop(id)
