import pandas as pd
import random

num_records = 50

names = [f'User{i}' for i in range(1, num_records + 1)]
locations = [random.choice(['New Delhi', 'Mumbai', 'Bengaluru', 'Chennai', 'Kolkata']) for _ in range(num_records)]
heights = [random.randint(150, 200) for _ in range(num_records)]  # Height in cm
weights = [random.randint(50, 120) for _ in range(num_records)]  # Weight in kg
ages = [random.randint(18, 70) for _ in range(num_records)]  # Age in years

user_data = pd.DataFrame({
    'Name': names,
    'Location': locations,
    'Height': heights,
    'Weight': weights,
    'Age': ages
})

csv_file_path = 'user_data.csv'
user_data.to_csv(csv_file_path, index=False)