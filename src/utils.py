from src.extract_text import load_data
from src.preprocess import clean_text
from src.features import get_features

def prepare_data(path):    
    data = load_data(path)
    data['cleaned'] = data['Resume'].apply(clean_text)
    X, vectorizer = get_features(data['cleaned'])
    y = data['Category']    
    return X, y, vectorizer