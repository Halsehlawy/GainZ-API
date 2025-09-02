from pydantic import BaseModel, Field
from typing import Optional

class ExerciseSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str
    sets: Optional[int] = None
    reps: Optional[str] = None
    weight: Optional[str] = None
    
    class Config:
        orm_mode = True

class ExerciseCreateSchema(BaseModel):
    name: str
    sets: Optional[int] = None
    reps: Optional[str] = None
    weight: Optional[str] = None

class ExerciseUpdateSchema(BaseModel):
    name: Optional[str] = None
    sets: Optional[int] = None
    reps: Optional[str] = None
    weight: Optional[str] = None

class WorkoutExerciseUpdateSchema(BaseModel):
    sets: Optional[int] = None
    reps: Optional[str] = None
    weight: Optional[str] = None
