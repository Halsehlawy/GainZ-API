from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):

    __abstract__ = True  # Prevents this class from being mapped to a database table

    id = Column(Integer, primary_key=True, index=True)

    # Specific columns for our Table.
    created_at = Column(DateTime, default=func.now())  # Timestamp for when the record was created
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Auto-updates on changes