# FastAPI ML Service

A high-performance machine learning microservice built with FastAPI for YouTube platform analytics, providing video recommendations, content moderation, and ad targeting capabilities.

## 🚀 Features

- **Video Recommendations**: AI-powered video recommendation engine based on user interaction data
- **Content Moderation**: Automated content safety analysis for video uploads
- **Ad Targeting**: Intelligent ad targeting based on user demographics and interests
- **Health Monitoring**: Built-in health check endpoints for service monitoring
- **CORS Support**: Cross-origin resource sharing for frontend integration
- **Comprehensive Logging**: Detailed logging for debugging and monitoring

## 📋 Prerequisites

- Python 3.11+
- pip package manager
- Virtual environment (recommended)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd fastapi-ml-service
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup ML Models
```bash
# Create models directory
mkdir -p app/models

# Train and save models (you'll need to implement train_models.py)
python train_models.py
```

## 🏃‍♂️ Running the Service

### Development Mode
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Using Docker
```bash
# Build the image
docker build -t fastapi-ml-service .

# Run the container
docker run -p 8000:8000 fastapi-ml-service
```

## 📡 API Endpoints

### Health Check
- **GET** `/` - Basic service status
- **GET** `/health` - Detailed health check with model status

### Machine Learning Services

#### Video Recommendations
- **POST** `/recommendations/`
- **Request Body**:
```json
{
  "user_id": 123,
  "video_id": 456,
  "watch_time": 120.5
}
```
- **Response**:
```json
{
  "recommended_video": 789,
  "user_id": 123,
  "confidence": 0.95
}
```

#### Content Moderation
- **POST** `/moderation/`
- **Request Body**:
```json
{
  "video_id": 456,
  "video_content": "Video content description or metadata"
}
```
- **Response**:
```json
{
  "moderation_result": 1,
  "video_id": 456,
  "content_length": 25,
  "is_safe": true
}
```

#### Ad Targeting
- **POST** `/ad-targeting/`
- **Request Body**:
```json
{
  "user_id": 123,
  "age": 25,
  "location": "New York",
  "interests": ["technology", "gaming", "music"]
}
```
- **Response**:
```json
{
  "recommended_ad": 1,
  "user_id": 123,
  "should_target": true,
  "user_profile": {
    "age": 25,
    "location": "New York",
    "interests_count": 3
  }
}
```

## 📁 Project Structure

```
fastapi-ml-service/
├── main.py                    # FastAPI application entry point
├── requirements.txt           # Python dependencies
├── train_models.py           # Model training script
├── Dockerfile                # Docker configuration
├── app/
│   ├── __init__.py
│   ├── models/               # Pre-trained ML models
│   │   ├── recommendation_model.joblib
│   │   ├── moderation_model.joblib
│   │   └── ad_targeting_model.joblib
│   └── schemas/              # Pydantic data models
│       ├── __init__.py
│       ├── recommendation.py
│       ├── moderation.py
│       └── ad_targeting.py
├── tests/                    # Unit tests
│   ├── __init__.py
│   └── test_endpoints.py
└── README.md
```

## 🧪 Testing

### Run Unit Tests
```bash
pytest tests/ -v
```

### Manual API Testing
```bash
# Test health endpoint
curl http://localhost:8000/health

# Test recommendation endpoint
curl -X POST "http://localhost:8000/recommendations/" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "video_id": 2, "watch_time": 120.5}'
```

## 🔧 Configuration

### Environment Variables
```bash
# Optional: Set custom port
export PORT=8000

# Optional: Set log level
export LOG_LEVEL=INFO
```

### CORS Configuration
The service is configured to allow requests from:
- `http://localhost:8080` (Spring Boot backend)
- `http://localhost:3000` (Frontend application)

Modify the CORS settings in `main.py` as needed for your environment.

## 📊 Model Information

### Recommendation Model
- **Input**: User ID, Video ID, Watch Time
- **Output**: Recommended Video ID with confidence score
- **Algorithm**: [Specify your algorithm here]

### Moderation Model
- **Input**: Video ID, Content metadata
- **Output**: Safety classification (0: unsafe, 1: safe)
- **Algorithm**: [Specify your algorithm here]

### Ad Targeting Model
- **Input**: User demographics and interests
- **Output**: Ad targeting decision
- **Algorithm**: [Specify your algorithm here]

## 🚀 Deployment

### Production Deployment
1. Build Docker image
2. Deploy to your container orchestration platform (Kubernetes, Docker Swarm, etc.)
3. Configure load balancer and health checks
4. Set up monitoring and logging

### Health Checks
The service includes built-in health check endpoints that can be used with:
- Docker health checks
- Kubernetes liveness/readiness probes
- Load balancer health checks

## 🔍 Monitoring & Logging

- All requests are logged with timestamps and user/video IDs
- Error handling with detailed error messages
- Health check endpoints for service monitoring
- Request/response logging for debugging

## 🤝 Integration

This service is designed to work with:
- **Spring Boot Backend**: RESTful API integration
- **Frontend Applications**: Direct API consumption
- **Other Microservices**: Service mesh integration

## 🆘 Support

For issues and questions:
- Create an issue in the GitHub repository
- Contact the development team
- Check the logs for detailed error information

## 🔄 Version History

- **v1.0.0**: Initial release with recommendation, moderation, and ad targeting services
