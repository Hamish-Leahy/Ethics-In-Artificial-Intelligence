# /ethics-in-artificial-intelligence/scripts/ethical_check.py

def check_for_bias(data):
    """
    Simple function to check for bias in the dataset.
    """
    bias_detected = False
    # Example: Check for gender bias in the dataset
    if 'gender' in data.columns:
        gender_counts = data['gender'].value_counts()
        if abs(gender_counts['Male'] - gender_counts['Female']) > len(data) * 0.1:
            bias_detected = True
    return bias_detected

if __name__ == "__main__":
    import pandas as pd

    input_path = '../data/cleaned_data.csv'
    data = pd.read_csv(input_path)
    
    if check_for_bias(data):
        print("Bias detected in the dataset.")
    else:
        print("No bias detected.")
