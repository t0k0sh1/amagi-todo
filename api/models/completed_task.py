from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class CompletedTask(Base):
    __tablename__ = "completed_tasks"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    completed_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

    task = relationship("Task", back_populates="completed_task")
