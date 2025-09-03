import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
jwt_secret = os.getenv("JWT_SECRET")
