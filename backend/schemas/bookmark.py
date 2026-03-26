from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime


class BookmarkBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    url: HttpUrl
    tags: list[str] = Field(default=[], max_length=10)


class BookmarkCreate(BookmarkBase):
    pass


class BookmarkUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    tags: Optional[list[str]] = None


class BookmarkResponse(BookmarkBase):
    id: int
    url: str
    tags: list[str]
    created_at: datetime
