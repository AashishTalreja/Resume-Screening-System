# This file is used to read resume text from CSV

import pandas as pd

def load_data(path):
    # reading csv file
    data = pd.read_csv(path)
    
    # assuming column name is 'Resume'
    return data