# Bookmark Saver

## What This Is
Learning project — bookmark saver app to practice FastAPI fundamentals before a hackathon.
Speed matters. Clarity over cleverness. No over-engineering.

## Stack
- **Backend:** Python 3.12+, FastAPI, Uvicorn, Pydantic v2 (managed with uv)
- **Frontend:** Next.js 14+ (App Router), TypeScript, Tailwind CSS (managed with bun)
- **Testing:** pytest + FastAPI TestClient
- **Database:** In-memory dict (swap to Postgres + SQLAlchemy only if time)

## Project Structure
```
BookmarkSaver/
├── backend/
│   ├── main.py              # App entry + CORS
│   ├── database.py          # In-memory store
│   ├── routers/
│   │   └── bookmarks.py     # All CRUD routes
│   ├── schemas/
│   │   └── bookmark.py      # Pydantic request/response models
│   └── tests/
│       └── test_bookmarks.py
└── frontend/
    ├── lib/api.ts           # All fetch calls to backend
    ├── components/
    │   ├── BookmarkForm.tsx  # Client component — add bookmark
    │   └── BookmarkList.tsx  # Client component — display + delete
    └── app/page.tsx         # Server component — fetches data
```

## Build Order
1. `GET /bookmarks` returning hardcoded data — verify at `/docs`
2. `POST /bookmarks` with Pydantic validation
3. `DELETE /bookmarks/{id}` with 404 handling
4. `GET /bookmarks?tag=work` query parameter filtering
5. Write tests for all 4 routes
6. Set up Next.js, create `lib/api.ts`
7. Build page — server component fetches, client components for form + list
8. Stretch: SQLAlchemy + Postgres with `Depends(get_db)`

## Rules
- Every route uses `response_model` with a Pydantic schema
- Schemas live in `schemas/`, never inline in router files
- One router file per resource
- Frontend fetches go through `lib/api.ts`, never inline in components
- Server Components for fetching, Client Components only for interactivity
- `status_code=201` on POST, `status_code=204` on DELETE
- Test each route immediately after writing it

## Mistakes to Watch For
- Using pip or npm — always use `uv` for Python and `bun` for frontend
- Missing CORS middleware — frontend fails silently
- Putting Pydantic models in the router file instead of schemas/
- Returning raw dicts instead of using response_model
- Hardcoding API URLs in frontend components instead of using lib/api.ts
- Using `"use client"` on the main page when a server component works
- Forgetting `status_code` on POST and DELETE decorators

## Commands
```bash
# Backend
cd backend
uv init && uv add fastapi[standard] pytest
uv run uvicorn main:app --reload --port 8000

# Tests
cd backend
uv run pytest tests/ -v

# Frontend
cd frontend
bun create next-app . --app --ts --tailwind --eslint --src-dir=false --import-alias="@/*"
bun dev
```