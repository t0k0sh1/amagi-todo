from typing import Optional

from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class TaskBase(BaseModel):
    title: str = Field(..., example="Buy groceries")
    due_date: Optional[datetime] = Field(None, example="2021-08-01T12:00:00")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="Whether the task is done or not")

    class Config:
        orm_mode = True
