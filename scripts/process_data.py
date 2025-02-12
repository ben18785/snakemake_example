import pandas as pd

# Read raw data
df = pd.read_csv("data/raw_data.csv")

# Simple transformation
df["C"] = df["A"] + df["B"]

# Save processed data
df.to_csv("data/processed_data.csv", index=False)
print("Data processed successfully!")