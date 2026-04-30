# basic preprocessing for structured data

def encode_education(data):
    
    # manually encoding (simple way)
    mapping = {
        "High School": 0,
        "Bachelors": 1,
        "Masters": 2
    }
    
    data['education_level'] = data['education_level'].map(mapping)
    
    return data