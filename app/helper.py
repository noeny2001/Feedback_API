import logging
from fastapi import HTTPException

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_error(message: str):
    logger.error(message)

def raise_http_exception(status_code: int, detail: str):
    log_error(detail)
    raise HTTPException(status_code=status_code, detail=detail)

def validate_rating(rating: int):
    if rating < 1 or rating > 5:
        raise_http_exception(400, "Rating must be between 1 and 5")
