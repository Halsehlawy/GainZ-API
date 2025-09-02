from pydantic import BaseModel, Field
from typing import Optional, List
from .user import UserResponseSchema

class ProgramSchema(BaseModel):
    id: Optional[int]=Field(default=None)
    name: str
    is_default: bool
    
    user: Optional[UserResponseSchema] = None
    
    class Config:
        orm_mode = True
        
class ProgramCreateSchema(BaseModel):
    name: str
    is_default: bool = False
