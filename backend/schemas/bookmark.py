from pydantic import BaseModel, HttpUrl
from datetime import datetime


class BookmarkCreate(BaseModel):
    name: str
    url: HttpUrl
    tags: list[str] = []


class BookmarkResponse(BaseModel):
    id: int
    name: str
    url: str
    tags: list[str]
    created_at: datetime
