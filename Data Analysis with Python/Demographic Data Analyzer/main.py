import pandas as pd
from demographic_data_analyzer import calculate_demographic_data

df = pd.read_csv('adult.data.csv')  # Replace with your CSV path
results = calculate_demographic_data(df)
print(results)
