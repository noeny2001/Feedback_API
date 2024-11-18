from pydantic import BaseModel, Field

class RatingRequest(BaseModel):
    user_id: str = Field(..., description="The ID of the user providing feedback")
    agent_code: str = Field(..., description="The code of the agent being rated")
    rating: int = Field(..., ge=1, le=5, description="Rating value between 1 and 5")

    class Config:
        schema_extra = {
            "example": {
                "user_id": "12345",
                "agent_code": "AGENT001",
                "rating": 5
            }
        }
