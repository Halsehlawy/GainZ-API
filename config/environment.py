import os
from dotenv import load_dotenv

load_dotenv()

db_URI = os.getenv("DB_URI")
jwt_secret = os.getenv("JWT_SECRET")
