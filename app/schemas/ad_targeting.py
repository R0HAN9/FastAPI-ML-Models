from pydantic import BaseModel
from typing import List

# Define the schema for the Ad Targeting API request using Pydantic
# This schema ensures the incoming request data is properly validated
 
class AdTargetingRequest(BaseModel):
    """
    Schema for an ad-targeting request.
    
    Attributes:
        user_id (int): Unique identifier for the user.
        age (int): Age of the user.
        location (str): Location of the user as a string.
        interests (List[str]): List of interests or hobbies of the user.
    """
    user_id: int  # Unique user ID for tracking and personalization
    age: int  # Age of the user, used for demographic targeting
    location: str  # User's location (e.g., city, state, or country)
    interests: List[str]  # List of user interests (e.g., ["sports", "music"])
