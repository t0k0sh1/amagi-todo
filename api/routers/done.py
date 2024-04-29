from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.services.done as done_service
from api.db import get_db

router = APIRouter()


@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_service.get_done(db, task_id=task_id)
    if done is not None:
        raise HTTPException(status_code=400, detail="Task is already done")

    return await done_service.mark_done(db, task_id=task_id)


@router.delete("/tasks/{task_id}/done", response_model=None)
async def mark_task_undone(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_service.get_done(db, task_id=task_id)
    if done is None:
        raise HTTPException(status_code=400, detail="Task is not done")

    return await done_service.unmark_done(db, done)
