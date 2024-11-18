import json
from fastapi import APIRouter, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.config import get_db
from .models import Rating  # Importing the model
from .helper import validate_rating, raise_http_exception
from .request import RatingRequest  # Import the Pydantic model

class FeedbackRouter:
     def __init__(self):
      self.router = APIRouter(prefix="/v1/cloud", tags=["feedback_router"])
      self.router.post("/feedback_rating")(self.feedback_rating)

     async def feedback_rating(self, rating_request: RatingRequest, db: Session = Depends(get_db)):
                  
                  
                  print(rating_request.user_id)
                  print(rating_request.agent_code)
                  print(rating_request.rating)
        # Validate the rating

                 # Create a new rating record
                  db_rating = Rating(
                  user_id=rating_request.user_id,
                  agent_code=rating_request.agent_code,
                  rating=rating_request.rating
                 )

     # Add and commit the new rating to the database
                  db.add(db_rating)
                  db.commit()

                    # Refresh to get the latest data from the DB
                  json_compatible_item_data = jsonable_encoder(rating_request)
    
                    # Step 4: Convert to string
                  json_string = json.dumps(json_compatible_item_data)
                  return {"message": "Rating submitted successfully", "data":  json_string}
     
        
     
     # Define the POST endpoint
    


feedback_router = FeedbackRouter()