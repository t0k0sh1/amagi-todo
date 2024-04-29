from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models as models


async def get_done(db: AsyncSession, task_id: int) -> models.CompletedTask | None:
    result: Result = await db.execute(
        select(models.CompletedTask).where(models.CompletedTask.id == task_id)
    )
    return result.scalars().first()


async def mark_done(db: AsyncSession, task_id: int) -> models.CompletedTask:
    done = models.CompletedTask(id=task_id)
    db.add(done)
    await db.commit()
    await db.refresh(done)
    return done


async def unmark_done(db: AsyncSession, original: models.CompletedTask) -> None:
    await db.delete(original)
    await db.commit()
