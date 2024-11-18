from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

# Declare a Base for the models
Base = declarative_base()

class Rating(Base):
    __tablename__ = "tbl_feedback_ratings"
    
    user_id = Column(String,primary_key=True, nullable=False)
    agent_code = Column(String(50), nullable=True)
    rating = Column(String, nullable=True)
