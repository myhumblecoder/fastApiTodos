from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class TodoBase(BaseModel):
    title: str
    completed: Optional[bool] = False
    priority: Optional[str] = "medium"
    due_date: Optional[date] = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True

class TodoList(BaseModel):
    todos: List[Todo]