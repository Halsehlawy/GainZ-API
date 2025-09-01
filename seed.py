# seed.py

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from config.environment import db_URI
from models.base import Base
# Import all models first to ensure they're registered
from models.user import UserModel
from models.program import ProgramModel
# Then import the data
from data.user_data import user_list
from data.program_data import program_list

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

# This seed file is a separate program that can be used to "seed" our database with some initial data.
try:
    print("Recreating database...")
    # Dropping (or deleting) the tables and creating them again is for convenience. Once we start to play around with
    # our data, changing our models, this seed program will allow us to rapidly throw out the old data and replace it.
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("seeding the database...")
    db = SessionLocal()

    # Seed users first (since programs reference users)
    db.add_all(user_list)
    db.commit()
    
    # Seed programs
    db.add_all(program_list)
    db.commit()

    db.close()

    print("Database seeding complete! ")
except Exception as e:
    print("An error occurred:", e)
