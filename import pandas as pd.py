import pandas as pd
import numpy as np

# Sample DataFrame for demonstration
data = {
    'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'North', 'South'],
    'Category': ['Electronics', 'Clothing', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Electronics', 'Clothing'],
    'Customer_Type': ['Retail', 'Wholesale', 'Retail', 'Retail', 'Wholesale', 'Wholesale', 'Retail', 'Retail'],
    'Sales': [1500, 800, 1200, 2500, 950, 3000, 1100, 700],
    'Quantity': [3, 10, 5, 4, 8, 6, 2, 9]
}
df = pd.DataFrame(data)

# --- Pivot Table ---
# Aggregating Sales by Region and Category, showing mean and sum
pivot_table = pd.pivot_table(
    df, 
    values='Sales', 
    index=['Region'], 
    columns=['Category'], 
    aggfunc=[np.sum, np.mean], 
    fill_value=0
)
print("--- Pivot Table ---")
print(pivot_table)

# --- Cross Tabulation (Crosstab) ---
# Frequency table of Region vs Customer Type
cross_tab = pd.crosstab(
    df['Region'], 
    df['Customer_Type'], 
    margins=True, 
    margins_name='Total'
)
print("\n--- Cross Tabulation ---")
print(cross_tab)