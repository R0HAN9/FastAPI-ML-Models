from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from app.schemas import recommendation, moderation, ad_targeting

# Load the saved models
recommendation_model = joblib.load('app/models/recommendation_model.joblib')
moderation_model = joblib.load('app/models/moderation_model.joblib')
ad_targeting_model = joblib.load('app/models/ad_targeting_model.joblib')

app = FastAPI()

@app.get("/")
def read_root():
    return {"FastAPI Machine Learning Models"}

# Endpoint for video recommendation
@app.post("/recommendations/")
async def recommend(request: recommendation.RecommendationRequest):
    input_data = np.array([[request.user_id, request.video_id, request.watch_time]])
    prediction = recommendation_model.predict(input_data)
    return {"recommended_video": int(prediction[0])}

# Endpoint for content moderation
@app.post("/moderation/")
async def moderate(request: moderation.ModerationRequest):
    input_data = np.array([[request.video_id, len(request.video_content)]])
    prediction = moderation_model.predict(input_data)
    return {"moderation_result": int(prediction[0])}

# Endpoint for ad targeting
@app.post("/ad-targeting/")
async def ad_targeting(request: ad_targeting.AdTargetingRequest):
    input_data = np.array([[request.user_id, request.age, len(request.location), len(request.interests)]])
    prediction = ad_targeting_model.predict(input_data)
    return {"recommended_ad": int(prediction[0])}
