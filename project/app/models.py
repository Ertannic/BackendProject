from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class User(BaseModel):
    username: str
    password: str

class UserInDB(User):
    pass

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in progress"
    DONE = "done"

class Task(BaseModel):
    id: str
    title: str
    description: str
    status: TaskStatus = Field(default=TaskStatus.TODO)
    createdAT: datetime
    updatedAT: datetime

class TaskCreate(BaseModel):
    title: str
    description: str
    status: Optional[TaskStatus] = TaskStatus.TODO

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[TaskStatus]

