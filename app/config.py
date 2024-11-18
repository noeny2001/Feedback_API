import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def create_db_engine():
    try:
        # Get DATABASE_URL from environment variables
        database_url = "postgresql://postgres:admin@localhost/feedback"
        print('Database URL:', database_url)  # Debugging line to check URL
        if database_url is None:
            raise ValueError("DATABASE_URL environment variable is not set")

        # Create and return SQLAlchemy engine
        engine = create_engine(
            database_url # Optional: Check connection before using
        )
        print("Connection established successfully to PostgreSQL")
        return engine
    except Exception as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

# Create the engine only once
engine = create_db_engine()

# Use the created engine in the sessionmaker
SessionLocal = sessionmaker(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
