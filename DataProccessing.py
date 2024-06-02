# /ethics-in-artificial-intelligence/scripts/data_preprocessing.py

import pandas as pd

def load_data(file_path):
    """
    Load CSV data from the specified file path.
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Clean the data by removing duplicates and handling missing values.
    """
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')
    return df

def save_data(df, output_path):
    """
    Save the cleaned data to the specified output path.
    """
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_path = '../data/example_data.csv'
    output_path = '../data/cleaned_data.csv'
    
    data = load_data(input_path)
    cleaned_data = clean_data(data)
    save_data(cleaned_data, output_path)
    print("Data preprocessing complete.")
