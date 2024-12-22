import joblib
from sklearn.ensemble import RandomForestClassifier

# Dummy training data for recommendation (user_id, video_id, watch_time)
X_rec = [[1, 1, 10], [1, 2, 15], [2, 1, 8], [2, 2, 25], [3, 3, 30], [3, 4, 5]]
y_rec = [1, 0, 1, 0, 1, 0]  # 1 = recommend, 0 = don't recommend
model_rec = RandomForestClassifier(n_estimators=100)
model_rec.fit(X_rec, y_rec)
joblib.dump(model_rec, 'app/models/recommendation_model.joblib')
print("Recommendation model saved!")

# Dummy training data for content moderation (video_id, content_length)
X_mod = [[1, 200], [2, 150], [3, 100], [4, 250]]
y_mod = [1, 0, 1, 0]  # 1 = safe, 0 = not safe
model_mod = RandomForestClassifier(n_estimators=100)
model_mod.fit(X_mod, y_mod)
joblib.dump(model_mod, 'app/models/moderation_model.joblib')
print("Moderation model saved!")

# Dummy training data for ad targeting (user_id, age, location_length, interests_count)
X_ad = [[1, 25, 5, 3], [2, 30, 4, 2], [3, 22, 6, 1], [4, 35, 7, 5], [5, 40, 3, 2], [6, 28, 6, 4]]
y_ad = [1, 0, 1, 0, 1, 0]  # 1 = target ad, 0 = don't target ad
model_ad = RandomForestClassifier(n_estimators=100)
model_ad.fit(X_ad, y_ad)
joblib.dump(model_ad, 'app/models/ad_targeting_model.joblib')
print("Ad targeting model saved!")
