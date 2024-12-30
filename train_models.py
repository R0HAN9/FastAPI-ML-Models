import joblib
from sklearn.ensemble import RandomForestClassifier

# --- Recommendation Model Training ---
# Dummy training data: Represents user interactions with videos
# Columns: [user_id, video_id, watch_time]
X_rec = [
    [1, 1, 10],  # User 1 watched Video 1 for 10 minutes
    [1, 2, 15],  # User 1 watched Video 2 for 15 minutes
    [2, 1, 8],   # User 2 watched Video 1 for 8 minutes
    [2, 2, 25],  # User 2 watched Video 2 for 25 minutes
    [3, 3, 30],  # User 3 watched Video 3 for 30 minutes
    [3, 4, 5],   # User 3 watched Video 4 for 5 minutes
]
y_rec = [
    1,  # Recommend Video 1
    0,  # Don't recommend Video 2
    1,  # Recommend Video 1
    0,  # Don't recommend Video 2
    1,  # Recommend Video 3
    0,  # Don't recommend Video 4
]

# Initialize and train a Random Forest model for recommendations
model_rec = RandomForestClassifier(n_estimators=100)
model_rec.fit(X_rec, y_rec)

# Save the trained recommendation model to a file for later use
joblib.dump(model_rec, 'app/models/recommendation_model.joblib')
print("Recommendation model saved!")

# --- Content Moderation Model Training ---
# Dummy training data: Represents video characteristics for moderation
# Columns: [video_id, content_length]
X_mod = [
    [1, 200],  # Video 1 has a content length of 200 characters
    [2, 150],  # Video 2 has a content length of 150 characters
    [3, 100],  # Video 3 has a content length of 100 characters
    [4, 250],  # Video 4 has a content length of 250 characters
]
y_mod = [
    1,  # Video 1 is marked as safe
    0,  # Video 2 is not safe
    1,  # Video 3 is marked as safe
    0,  # Video 4 is not safe
]

# Initialize and train a Random Forest model for content moderation
model_mod = RandomForestClassifier(n_estimators=100)
model_mod.fit(X_mod, y_mod)

# Save the trained moderation model to a file for later use
joblib.dump(model_mod, 'app/models/moderation_model.joblib')
print("Moderation model saved!")

# --- Ad Targeting Model Training ---
# Dummy training data: Represents user characteristics for ad targeting
# Columns: [user_id, age, location_length, interests_count]
X_ad = [
    [1, 25, 5, 3],  # User 1: Age 25, location length 5, interests count 3
    [2, 30, 4, 2],  # User 2: Age 30, location length 4, interests count 2
    [3, 22, 6, 1],  # User 3: Age 22, location length 6, interests count 1
    [4, 35, 7, 5],  # User 4: Age 35, location length 7, interests count 5
    [5, 40, 3, 2],  # User 5: Age 40, location length 3, interests count 2
    [6, 28, 6, 4],  # User 6: Age 28, location length 6, interests count 4
]
y_ad = [
    1,  # Target ad to User 1
    0,  # Don't target ad to User 2
    1,  # Target ad to User 3
    0,  # Don't target ad to User 4
    1,  # Target ad to User 5
    0,  # Don't target ad to User 6
]

# Initialize and train a Random Forest model for ad targeting
model_ad = RandomForestClassifier(n_estimators=100)
model_ad.fit(X_ad, y_ad)

# Save the trained ad targeting model to a file for later use
joblib.dump(model_ad, 'app/models/ad_targeting_model.joblib')
print("Ad targeting model saved!")
