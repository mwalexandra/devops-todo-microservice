from datetime import date
from typing import Optional

from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: str = "todo"

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[str] = None

class TodoRead(TodoBase):
    id: int

    class Config:
        from_attributes = True