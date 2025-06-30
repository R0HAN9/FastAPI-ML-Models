# main.py - FastAPI ML Service

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import logging
from pathlib import Path

from app.schemas.recommendation import RecommendationRequest
from app.schemas.moderation import ModerationRequest
from app.schemas.ad_targeting import AdTargetingRequest

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="YouTube ML Service",
    description="Machine Learning service for video recommendations, content moderation, and ad targeting",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:3000"],  # Add your Spring Boot and frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ML models
try:
    recommendation_model = joblib.load('app/models/recommendation_model.joblib')
    moderation_model = joblib.load('app/models/moderation_model.joblib')
    ad_targeting_model = joblib.load('app/models/ad_targeting_model.joblib')
    logger.info("All ML models loaded successfully")
except Exception as e:
    logger.error(f"Error loading models: {e}")
    raise

@app.get("/")
def read_root():
    """Health check endpoint"""
    return {"message": "FastAPI ML Service is running", "status": "healthy"}

@app.get("/health")
def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": "FastAPI ML Service",
        "models_loaded": {
            "recommendation": recommendation_model is not None,
            "moderation": moderation_model is not None,
            "ad_targeting": ad_targeting_model is not None
        }
    }

@app.post("/recommendations/")
async def get_recommendations(request: RecommendationRequest):
    """
    Get video recommendations based on user interaction data
    """
    try:
        logger.info(f"Recommendation request for user_id: {request.user_id}")
        
        # Prepare input data for the model
        input_data = np.array([[request.user_id, request.video_id, request.watch_time]])
        
        # Make prediction
        prediction = recommendation_model.predict(input_data)
        
        response = {
            "recommended_video": int(prediction[0]),
            "user_id": request.user_id,
            "confidence": float(recommendation_model.predict_proba(input_data)[0].max())
        }
        
        logger.info(f"Recommendation successful: {response}")
        return response
        
    except Exception as e:
        logger.error(f"Error in recommendation: {e}")
        raise HTTPException(status_code=500, detail=f"Recommendation failed: {str(e)}")

@app.post("/moderation/")
async def moderate_content(request: ModerationRequest):
    """
    Moderate video content for safety
    """
    try:
        logger.info(f"Moderation request for video_id: {request.video_id}")
        
        # Prepare input data for the model
        content_length = len(request.video_content) if request.video_content else 0
        input_data = np.array([[request.video_id, content_length]])
        
        # Make prediction
        prediction = moderation_model.predict(input_data)
        
        response = {
            "moderation_result": int(prediction[0]),
            "video_id": request.video_id,
            "content_length": content_length,
            "is_safe": bool(prediction[0] == 1)
        }
        
        logger.info(f"Moderation successful: {response}")
        return response
        
    except Exception as e:
        logger.error(f"Error in moderation: {e}")
        raise HTTPException(status_code=500, detail=f"Moderation failed: {str(e)}")

@app.post("/ad-targeting/")
async def target_ads(request: AdTargetingRequest):
    """
    Target ads based on user profile
    """
    try:
        logger.info(f"Ad targeting request for user_id: {request.user_id}")
        
        # Prepare input data for the model
        location_length = len(request.location) if request.location else 0
        interests_count = len(request.interests) if request.interests else 0
        input_data = np.array([[request.user_id, request.age, location_length, interests_count]])
        
        # Make prediction
        prediction = ad_targeting_model.predict(input_data)
        
        response = {
            "recommended_ad": int(prediction[0]),
            "user_id": request.user_id,
            "should_target": bool(prediction[0] == 1),
            "user_profile": {
                "age": request.age,
                "location": request.location,
                "interests_count": interests_count
            }
        }
        
        logger.info(f"Ad targeting successful: {response}")
        return response
        
    except Exception as e:
        logger.error(f"Error in ad targeting: {e}")
        raise HTTPException(status_code=500, detail=f"Ad targeting failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
