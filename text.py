import pandas as pd
import matplotlib.pyplot as plt

# Load metadata file
meta = pd.read_csv("country.csv")

# Count countries by IncomeGroup
income_counts = meta['IncomeGroup'].value_counts()

# Create a stylish bar chart
plt.figure(figsize=(10,6))
bars = plt.bar(income_counts.index, income_counts.values,
               color=['#FF9999','#66B2FF'],
               edgecolor='black')

# Add title and labels with better font styling
plt.title("Distribution of Countries by Income Group", fontsize=16, fontweight='bold')
plt.xlabel("Income Group", fontsize=12)
plt.ylabel("Number of Countries", fontsize=12)

# Rotate x-axis labels for readability
plt.xticks(rotation=20, fontsize=11)
plt.yticks(fontsize=11)

# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval),
             ha='center', va='bottom', fontsize=11, fontweight='bold')

# Add gridlines for clarity
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()