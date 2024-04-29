from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

import api.models as model
import api.schemas.task as task_schema


async def create_task(db: AsyncSession, task_create: task_schema.TaskCreate) -> model.Task:
    task = model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_tasks_with_done(db: AsyncSession) -> list[tuple[int, str, bool]]:
    result: Result = await db.execute(
        select(
            model.Task.id,
            model.Task.title,
            model.Task.due_date,
            model.CompletedTask.id.isnot(None).label("done"),
        ).outerjoin(model.CompletedTask)
    )

    return result.all()


async def get_task(db: AsyncSession, task_id: int) -> model.Task:
    result: Result = await db.execute(
        select(
            model.Task
        ).filter(model.Task.id == task_id)
    )

    return result.scalars().first()


async def update_task(db: AsyncSession, task_id: int, task_update: task_schema.TaskCreate) -> model.Task:
    task = get_task(db, task_id)
    for key, value in task_update.dict().items():
        setattr(task, key, value)
    await db.commit()
    await db.refresh(task)
    return task


async def delete_task(db: AsyncSession, task_id: int) -> None:
    db.query(model.Task).filter(model.Task.id == task_id).delete()
    await db.commit()
