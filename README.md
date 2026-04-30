# Resume Screening System (ML + Python)

This is a simple machine learning project that classifies resumes into categories.

## Steps:
1. Load dataset
2. Clean text
3. Convert text to features (TF-IDF)
4. Train model (Naive Bayes)
5. Predict category

## How to run:

1. Install requirements:
   pip install -r requirements.txt

2. Train model:
   (run manually in Python)
   from src.utils import prepare_data
   from src.train_model import train_model, save_model

   X, y, vectorizer = prepare_data("data/Resume.csv")
   model = train_model(X, y)
   save_model(model, vectorizer)

3. Run app:
   streamlit run app/app.py