from fastapi import FastAPI
from .routes import tracker
from .database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tracker.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://learning-tracker-6dhpu0sss-venislausashishs-projects.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)