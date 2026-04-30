import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pickle
import os
from src.preprocess import encode_education

def train():
    print("Training started...")

    # load dataset
    data = pd.read_csv("data/ai_resume_screening.csv")

    # encode education
    data['education_level'] = data['education_level'].astype(str)
    data = encode_education(data)

    # split features and target
    X = data.drop("shortlisted", axis=1)
    y = data["shortlisted"]

    # convert features to numeric
    X = X.apply(pd.to_numeric, errors='coerce')

    # remove rows with NaN
    X = X.dropna()
    y = y.loc[X.index]

    # convert target
    y = y.map({"No": 0, "Yes": 1})

    # split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )

    # scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # train model
    model = LogisticRegression(max_iter=1000, class_weight='balanced')
    model.fit(X_train, y_train)

    print("Model trained successfully")

    # create models folder
    if not os.path.exists("models"):
        os.makedirs("models")

    # save model
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    # save scaler
    with open("models/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)