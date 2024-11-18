from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from .models import Base, Rating  # Importing the model from models.py
from .models import Base, Rating
from .config import engine  


# Create the database tables
def init_db():
    Base.metadata.create_all(bind=engine)
