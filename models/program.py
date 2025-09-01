from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .user import UserModel

class ProgramModel(BaseModel):
    __tablename__="programs"
    
    id = Column(Integer,primary_key=True, index=True)
    
    #Program Columns
    name = Column(String, unique=True)
    is_default = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    #Relationships
    user = relationship('UserModel', back_populates='programs')
    workouts = relationship('WorkoutModel', back_populates='program', cascade='all, delete-orphan')
    
    