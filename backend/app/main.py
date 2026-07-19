from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app import models
from app.seed import seed_database
from app.routers import home
from app.routers import lessons
from app.routers import profile
from app.routers import leaderboard

Base.metadata.create_all(bind=engine)

seed_database()

app = FastAPI(
    title="Duolingo Clone API",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home.router)
app.include_router(lessons.router)
app.include_router(profile.router)
app.include_router(leaderboard.router)


@app.get("/")
def root():
    return {
        "message": "Duolingo Clone Backend Running"
    }