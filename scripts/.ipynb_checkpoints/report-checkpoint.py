import pandas as pd

# Read processed data
df = pd.read_csv("data/processed_data.csv")

# Generate a simple summary report
summary = df.describe()
summary.to_csv("data/report.csv")
print("Report generated successfully!")