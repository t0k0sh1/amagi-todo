from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(..., example="Buy groceries")


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
