from pydantic import BaseModel

class ModerationRequest(BaseModel):
    video_id: int
    video_content: str
