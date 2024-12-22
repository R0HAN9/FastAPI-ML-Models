from pydantic import BaseModel
from typing import List

class AdTargetingRequest(BaseModel):
    user_id: int
    age: int
    location: str
    interests: List[str]
