import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Superstore dataset
df = pd.read_csv("Sample - Superstore.csv")

# Display first five rows
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())
# Generate descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())# Calculate total sales and profit
print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())# Category-wise Sales Analysis
print("\nCategory-wise Sales:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))# Category-wise Profit Analysis
print("\nCategory-wise Profit:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))# Region-wise Sales Analysis
print("\nRegion-wise Sales:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))
# Region-wise Profit Analysis
print("\nRegion-wise Profit:")
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))
# Top 10 Products by Sales
print("\nTop 10 Products by Sales:")
print(
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
# Monthly Sales Analysis
df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Month"] = df["Order Date"].dt.to_period("M")

print("\nMonthly Sales Analysis:")
print(df.groupby("Month")["Sales"].sum())
# Year-wise Sales Analysis
df["Year"] = df["Order Date"].dt.year

print("\nYear-wise Sales Analysis:")
print(df.groupby("Year")["Sales"].sum().sort_values(ascending=False))
# Profit Analysis by Region and Category
print("\nProfit by Region and Category:")
print(df.groupby(["Region", "Category"])["Profit"].sum())
# Discount and Profit Analysis
print("\nDiscount and Profit Analysis:")

print(
    df.groupby("Discount")[["Sales", "Profit"]]
    .mean()
    .round(2)
)
# Category-wise Sales Visualization
import matplotlib.pyplot as plt

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")

plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()
# Region-wise Sales Visualization

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("region_sales.png")
plt.show()
# Category-wise Profit Visualization

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")

plt.title("Profit by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("category_profit.png")
plt.show()
# Sales by Customer Segment Visualization

segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
segment_sales.plot(kind="bar")

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("segment_sales.png")
plt.show()
# Sales by Sub-Category Visualization

subcategory_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
subcategory_sales.plot(kind="bar")

plt.title("Sales by Product Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("subcategory_sales.png")
plt.show()
# Correlation Analysis

print("\n--- Correlation Analysis ---")

numerical_data = df[
    ["Sales", "Quantity", "Discount", "Profit"]
]

correlation_matrix = numerical_data.corr()

print(correlation_matrix)

# Correlation Heatmap

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap of Superstore Dataset")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()
# Outlier Detection using IQR Method

print("\n--- Outlier Detection ---")

columns_to_check = ["Sales", "Profit", "Quantity", "Discount"]

for column in columns_to_check:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print(f"\nColumn: {column}")
    print(f"Lower Bound: {lower_bound:.2f}")
    print(f"Upper Bound: {upper_bound:.2f}")
    print(f"Number of Outliers: {len(outliers)}")

# Save Outlier Analysis Results

outlier_summary = []

for column in columns_to_check:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    count = (
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ).sum()

    outlier_summary.append({
        "Column": column,
        "Lower Bound": lower_bound,
        "Upper Bound": upper_bound,
        "Outlier Count": count
    })

outlier_summary_df = pd.DataFrame(outlier_summary)
outlier_summary_df.to_csv("outlier_summary.csv", index=False)

print("\nOutlier summary saved to outlier_summary.csv")
import pandas as pd
import matplotlib.pyplot as plt

# Load the Superstore dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# Calculate sales by customer segment
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

# Create the bar chart
plt.figure(figsize=(8, 5))
segment_sales.plot(kind="bar")

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=0)
plt.tight_layout()

# Save the chart
plt.savefig("segment_sales.png", dpi=300, bbox_inches="tight")
plt.show()

print(segment_sales)
print("Chart saved as segment_sales.png")
