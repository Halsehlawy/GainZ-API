from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from controllers.programs import router as ProgramsRouter
from controllers.users import router as UsersRouter
app = FastAPI()

# ✅ Allow your React dev server(s) to call the API
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # Later, add your deployed frontend origin, e.g.:
    # "https://your-frontend.example.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # Which sites can call this API
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],       # Allow all headers (e.g., Content-Type, Authorization)
    # NOTE: We are NOT using credentials in this simple lesson,
    # so we are not setting allow_credentials.
)

app.include_router(ProgramsRouter, prefix='/api')
app.include_router(UsersRouter, prefix='/api')

# Health check endpoint
@app.get("/health")
def health_check():
    return {"ok": True}