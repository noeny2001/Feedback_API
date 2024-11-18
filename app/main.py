from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.feedback import FeedbackRouter
from app.init_db import init_db
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app.config import create_db_engine
from app.feedback import FeedbackRouter

class FeedbackRating(FastAPI):
    def __init__(self):
        super().__init__(
            debug=True,
            docs_url="/v1/cloud/docs",
            redoc_url="/v1/cloud/redoc",
            openapi_url="/v1/cloud/openapi.json",
            contact={
                "name": "Feedback_Rating",
                "url": "https://www.binarytest.com"
            }
        )

        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Create database engine
        self.engine = create_db_engine()  # Ensure this is defined correctly
        Base.metadata.create_all(bind=self.engine)  # Create tables
        init_db()  # Ensure this uses the correct engine if needed
        self.feedback_router = FeedbackRouter()
        self.include_router(self.feedback_router.router)

# Create an instance of the FeedbackRating app
app = FeedbackRating()

@app.get("/v1/ping")
async def read_root():
    return {"message": "Welcome to the TDP API"}
