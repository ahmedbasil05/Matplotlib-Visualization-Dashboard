"""
Matplotlib Visualization Dashboard
----------------------------------
This script showcases different types of plots 
using Python and Matplotlib.

Visualizations included:
1. Line Plot - Monthly Sales Trend
2. Scatter Plot - Age vs. Screen Time
3. Histogram - Exam Scores
4. Bar Chart - Product Sales
5. Pie Chart - Market Share

Author: Your Name
"""

import matplotlib.pyplot as plt

# Line plot data (monthly sales)
months = list(range(1, 13))
sales = [120, 135, 150, 160, 180, 210, 250, 270, 300, 280, 260, 240]

# Scatter plot data (age vs. screen time)
ages = [10, 12, 14, 15, 16, 18, 20, 22, 25, 30, 35, 40, 45, 50]
screen_time = [5, 6, 6.5, 7, 6.8, 6, 5.5, 5, 4, 3.5, 3, 2.5, 2, 1.5]

# Histogram data (exam scores)
exam_scores = [
    55, 60, 62, 65, 67, 70, 72, 73, 75, 78, 80,
    82, 84, 85, 87, 88, 90, 91, 93, 95, 97, 98
]

# Bar chart data (product sales)
products = ["Product A", "Product B", "Product C", "Product D"]
units_sold = [150, 230, 180, 120]

# Pie chart data (market share)
companies = ["Company A", "Company B", "Company C"]
market_share = [40, 35, 25]

# Create subplot grid (2 rows x 3 cols)
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle("Matplotlib Visualization Dashboard", fontsize=16, fontweight="bold")

# Line plot
axes[0, 0].plot(months, sales, marker="o", color="blue", linewidth=2, label="Sales")
axes[0, 0].set_title("Monthly Sales Trend")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Units Sold")
axes[0, 0].grid(True, linestyle="--", alpha=0.6)
axes[0, 0].legend()

# Scatter plot
axes[0, 1].scatter(ages, screen_time, s=80, color="green", alpha=0.7)
axes[0, 1].set_title("Age vs. Screen Time")
axes[0, 1].set_xlabel("Age (years)")
axes[0, 1].set_ylabel("Hours/day")

# Histogram
axes[0, 2].hist(exam_scores, bins=8, color="orange", edgecolor="black")
axes[0, 2].set_title("Exam Scores Distribution")
axes[0, 2].set_xlabel("Score Range")
axes[0, 2].set_ylabel("Students")

# Bar chart
axes[1, 0].bar(products, units_sold, color=["red", "green", "blue", "purple"])
axes[1, 0].set_title("Product Sales Comparison")
axes[1, 0].set_xlabel("Products")
axes[1, 0].set_ylabel("Units Sold")

# Pie chart
axes[1, 1].pie(market_share,labels=companies,autopct="%1.1f%%",startangle=90,colors=["red", "green", "blue"],
    explode=(0.05, 0.05, 0.05),
    shadow=True
)
axes[1, 1].set_title("Market Share Breakdown")

# Hide empty subplot (bottom-right)
axes[1, 2].axis("off")

# Adjust layout and display plots
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
