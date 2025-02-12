import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
df = pd.read_csv("data/processed_data.csv")

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(df["A"], df["B"], c=df["C"], cmap="viridis", edgecolors="k")
plt.colorbar(label="Sum of Values")
plt.xlabel("Value 1")
plt.ylabel("Value 2")
plt.title("Scatter Plot of Simulated Data")

# Save the plot
plt.savefig("figures/plot.png", dpi=300)
print("Plot saved as 'figures/plot.png'!")