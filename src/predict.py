import pickle
import pandas as pd

def load_model():
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("models/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    return model, scaler


def predict_candidate(data_dict):
    model, scaler = load_model()

    df = pd.DataFrame([data_dict])

    # ML prediction
    df_scaled = scaler.transform(df)
    ml_result = model.predict(df_scaled)[0]

    # 🔥 RULE-BASED BOOST (important)
    score = 0

    if data_dict["years_experience"] >= 2:
        score += 1
    if data_dict["skills_match_score"] >= 70:
        score += 1
    if data_dict["project_count"] >= 3:
        score += 1
    if data_dict["github_activity"] >= 50:
        score += 1

    # combine logic
    if ml_result == 1 or score >= 2:
        return "Shortlisted"
    else:
        return "Not Shortlisted"