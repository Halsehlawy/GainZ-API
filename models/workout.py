from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import BaseModel

class WorkoutModel(BaseModel):
    __tablename__ = "workouts"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Workout Columns
    name = Column(String, nullable=False)
    day_of_week = Column(Integer, nullable=False)
    exercise_ids = Column(JSON, nullable=True, default=[])
    program_id = Column(Integer, ForeignKey('programs.id'), nullable=False)
    
    # Relationships
    program = relationship('ProgramModel', back_populates='workouts')
