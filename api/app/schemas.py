from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    taskid: str
    title: Optional[str]
    params: dict = None
