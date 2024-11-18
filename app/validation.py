from fastapi import HTTPException

def validate_rating(rating: int):
    if rating < 1 or rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
