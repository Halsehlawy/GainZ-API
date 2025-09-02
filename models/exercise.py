from sqlalchemy import Column, Integer, String
from .base import BaseModel

class ExerciseModel(BaseModel):
    __tablename__ = "exercises"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Exercise Columns
    name = Column(String, nullable=False)
    sets = Column(Integer, nullable=True)
    reps = Column(String, nullable=True)
    weight = Column(String, nullable=True)
