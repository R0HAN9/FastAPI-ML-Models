from pydantic import BaseModel

# Define the schema for the Content Moderation API request using Pydantic
# This schema validates the incoming data for content moderation.

class ModerationRequest(BaseModel):
    """
    Schema for a content moderation request.
    
    Attributes:
        video_id (int): Unique identifier for the video.
        video_content (str): Content of the video as a string (e.g., transcript or description).
    """
    video_id: int  # Unique ID of the video to be moderated
    video_content: str  # The text content associated with the video (e.g., transcript, description)
