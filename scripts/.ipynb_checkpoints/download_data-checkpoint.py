import pandas as pd

# Simulate downloading data
df = pd.DataFrame({"A": range(10), "B": range(10, 20)})
df.to_csv("data/raw_data.csv", index=False)
print("Data downloaded successfully!")