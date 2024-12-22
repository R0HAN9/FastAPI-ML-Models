Run the FastAPI app:
uvicorn app.main:app --reload

Testing the API Endpoints:
We can test the API endpoints using Postman. Below are examples of the data you would send for each endpoint:

Recommendation Example:
POST /recommendations/

    {
        "user_id": 1,
        "video_id": 1,
        "watch_time": 15.5
    }

Moderation Example:
POST /moderation/

    {
        "video_id": 1,
        "video_content": "This is a safe video content."
    }

Ad Targeting Example:
POST /ad-targeting/

    {
        "user_id": 1,
        "age": 25,
        "location": "New York",
        "interests": ["Technology", "Music"]
    }
