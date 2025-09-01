from pydantic import BaseModel, Field
from typing import Optional

class WorkoutSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str
    day_of_week: int = Field(..., ge=1, le=7)
    program_id: int
    
    class Config:
        orm_mode = True

class WorkoutCreateSchema(BaseModel):
    name: str
    day_of_week: int = Field(..., ge=1, le=7)
    program_id: int

class WorkoutUpdateSchema(BaseModel):
    name: Optional[str] = None
    day_of_week: Optional[int] = Field(None, ge=1, le=7)
