from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result

import api.models.task as task_model
import api.schemas.task as task_schema


def create_task(db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
    task = task_model.Task(**task_create.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks_with_done(db: Session) -> list[tuple[int, str, bool]]:
    result: Result = db.execute(
        select(
            task_model.Task.id,
            task_model.Task.title,
            task_model.Done.id.isnot(None).label("done"),
        ).outerjoin(task_model.Done)
    )

    return result.all()


def get_task(db: Session, task_id: int) -> task_model.Task:
    result: Result = db.execute(
        select(
            task_model.Task
        ).filter(task_model.Task.id == task_id)
    )

    return result.scalars().first()


def update_task(db: Session, task_id: int, task_update: task_schema.TaskCreate) -> task_model.Task:
    task = get_task(db, task_id)
    for key, value in task_update.dict().items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task
