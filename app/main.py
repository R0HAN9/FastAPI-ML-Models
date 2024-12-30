from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from app.schemas import recommendation, moderation, ad_targeting

# Load pre-trained machine learning models
# These models are saved in the 'app/models/' directory and are loaded using joblib
recommendation_model = joblib.load('app/models/recommendation_model.joblib')  # Model for video recommendations
moderation_model = joblib.load('app/models/moderation_model.joblib')  # Model for content moderation
ad_targeting_model = joblib.load('app/models/ad_targeting_model.joblib')  # Model for ad targeting

# Initialize the FastAPI application
app = FastAPI()

# Root endpoint to check if the API is running
@app.get("/")
def read_root():
    """
    Root endpoint for health check.
    Returns a simple JSON response indicating the API is operational.
    """
    return {"FastAPI Machine Learning Models"}

# Endpoint for video recommendations
@app.post("/recommendations/")
async def recommend(request: recommendation.RecommendationRequest):
    """
    Predicts a recommended video for a user based on user and video data.

    Args:
        request (RecommendationRequest): User and video details including:
                                         - user_id
                                         - video_id
                                         - watch_time

    Returns:
        JSON response with the recommended video ID.
    """
    # Prepare input data for the recommendation model
    input_data = np.array([[request.user_id, request.video_id, request.watch_time]])
    
    # Make a prediction using the recommendation model
    prediction = recommendation_model.predict(input_data)
    
    # Return the recommended video ID
    return {"recommended_video": int(prediction[0])}

# Endpoint for content moderation
@app.post("/moderation/")
async def moderate(request: moderation.ModerationRequest):
    """
    Predicts the moderation status of a video based on its content.

    Args:
        request (ModerationRequest): Video details including:
                                     - video_id
                                     - video_content (length analyzed)

    Returns:
        JSON response with the moderation result (e.g., 0 for safe, 1 for flagged).
    """
    # Prepare input data for the moderation model
    input_data = np.array([[request.video_id, len(request.video_content)]])
    
    # Make a prediction using the moderation model
    prediction = moderation_model.predict(input_data)
    
    # Return the moderation result
    return {"moderation_result": int(prediction[0])}

# Endpoint for ad targeting
@app.post("/ad-targeting/")
async def ad_targeting(request: ad_targeting.AdTargetingRequest):
    """
    Predicts the most suitable ad for a user based on demographic and behavioral data.

    Args:
        request (AdTargetingRequest): User details including:
                                      - user_id
                                      - age
                                      - location
                                      - interests

    Returns:
        JSON response with the recommended ad ID.
    """
    # Prepare input data for the ad targeting model
    input_data = np.array([[request.user_id, request.age, len(request.location), len(request.interests)]])
    
    # Make a prediction using the ad targeting model
    prediction = ad_targeting_model.predict(input_data)
    
    # Return the recommended ad ID
    return {"recommended_ad": int(prediction[0])}
