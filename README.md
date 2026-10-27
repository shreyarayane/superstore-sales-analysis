# Superstore Sales Analysis

## Project Overview
This project focuses on analyzing Superstore sales data using Python to identify sales trends, profit performance, and business insights. The analysis helps understand product category performance, regional sales, and monthly sales patterns.

## Objectives
- Analyze sales and profit performance.
- Compare sales across product categories and regions.
- Explore monthly and yearly sales trends.
- Identify top-performing products.
- Create visualizations to present findings clearly.

## Tools and Technologies
- Python
- Pandas
- Matplotlib
- VS Code
- Git and GitHub

## Dataset
The project uses the Sample Superstore dataset, which contains 9,994 records and 21 columns related to orders, products, sales, discounts, profit, and regions.

## Data Analysis Performed
- Inspected dataset structure and column information.
- Checked missing values and duplicate records.
- Generated descriptive statistics.
- Calculated total sales and total profit.
- Analyzed sales and profit by product category.
- Analyzed sales and profit by region.
- Explored monthly and yearly sales.
- Examined sales and profit across discount levels.
- Identified the top 10 products by sales.

## Visualizations

### 1. Sales by Product Category
![Sales by Product Category](category_sales.png)

### 2. Sales by Region
![Sales by Region](region_sales.png)

### 3. Profit by Product Category
![Profit by Product Category](category_profit.png)

## Key Findings
The analysis of 9,994 Superstore records revealed the following business insights:

1. **Overall Performance:** Total sales were $2,297,200.86, with a total profit of $286,397.02.

2. **Regional Performance:** The West region recorded the highest sales ($725,457.82) and profit ($108,418.45).

3. **Category Performance:** Technology was the top-performing category, generating $836,154.03 in sales and $145,454.95 in profit.

4. **Data Quality:** No missing values or duplicate records were found.

5. **Discount Analysis:** Average profit was negative at several discount levels. At a 50% discount, average profit was -$310.70.

6. **Yearly Sales Trend:** 2017 recorded the highest annual sales, totaling $733,215.26.

**Business Recommendation:** Focus on high-performing regions and categories while reviewing discount policies to improve profitability.

## Project Files
- `analysis.py` — Python code for data analysis and visualizations.
- `Sample - Superstore.csv` — Dataset used for analysis.
- `category_sales.png` — Category-wise sales chart.
- `region_sales.png` — Region-wise sales chart.
- `category_profit.png` — Category-wise profit chart.

## How to Run
1. Install Python.
2. Install the required libraries:
   `python -m pip install pandas matplotlib`
3. Download or clone this repository.
4. Run the analysis:
   `python analysis.py`

## Conclusion
This project demonstrates the use of Python, Pandas, and Matplotlib for exploratory data analysis and business reporting. It provides practice in data inspection, sales and profit analysis, and data visualization.

## Author
Shreya Rayane
## Business Insights

1. **Overall Performance:** The Superstore dataset generated total sales of approximately $2.30 million and total profit of $286,397.

2. **Top Performing Region:** The West region recorded the highest sales, approximately $725,458, and the highest profit, approximately $108,418.

3. **Best Performing Category:** Technology generated the highest sales, approximately $836,154, and the highest profit, approximately $145,455.

4. **Furniture Profitability:** Furniture generated approximately $742,000 in sales but only $18,451 in profit. This indicates that its profitability needs improvement.

5. **Yearly Sales Trend:** Sales were highest in 2017, reaching approximately $733,215.

6. **Data Quality:** The dataset contains 9,994 records, with no missing values or duplicate records detected during the initial data-quality checks.

7. **Discount Impact:** The correlation between discount and profit was approximately -0.22, indicating a negative relationship between higher discounts and profit in this dataset. Correlation does not necessarily imply causation.

## Business Recommendations

1. **Improve Furniture Profitability:** Review Furniture product costs, pricing, shipping expenses, and discount policies to identify ways to increase profit margins.

2. **Optimize Discount Strategies:** Evaluate high-discount transactions and introduce discount limits where appropriate to reduce the risk of unprofitable sales.

3. **Focus on High-Performing Markets:** Study successful sales strategies in the West region and Technology category to identify practices that may work in other regions and categories.

## Conclusion

This project demonstrates how Python, Pandas, data visualization, statistical analysis, Git, GitHub, and Power BI can be used to analyze retail sales data. The analysis identifies sales trends, regional performance, category profitability, and the relationship between discounts and profit. The findings can help businesses make informed decisions about pricing, discounts, and sales strategies.

## Project Deliverables

- Python data analysis script (`analysis.py`)
- Superstore sales dataset (`Sample - Superstore.csv`)
- Sales and profit visualization charts
- Correlation heatmap
- Outlier analysis summary
- Power BI interactive dashboard (`Superstore_Sales_Analysis.pbix`)
- Project documentation and business recommendations
