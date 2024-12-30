from pydantic import BaseModel

# Define the schema for the Video Recommendation API request using Pydantic
# This schema ensures the incoming data for video recommendations is validated.

class RecommendationRequest(BaseModel):
    """
    Schema for a video recommendation request.
    
    Attributes:
        user_id (int): Unique identifier for the user making the request.
        video_id (int): Unique identifier for the video being considered.
        watch_time (float): The duration (in minutes) the user watched the video.
    """
    user_id: int  # Unique ID representing the user
    video_id: int  # Unique ID representing the video
    watch_time: float  # Time (in minutes) the user spent watching the video
