from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    user_id: int
    video_id: int
    watch_time: float
