#| C:\Users\hi\Desktop\vs python\restaurant_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Configuration & Data Loading ---

def load_data():
    """
    Loads all required CSV files into pandas DataFrames.
    """
    
    print("Collecting data and getting it ready for use.")
    try:
        # Load Sales Data
        df_week1 = pd.read_csv(r"C:\Users\hi\Desktop\vs python\Restaurant - Week 1 Sales.csv")
        df_week2 = pd.read_csv(r"C:\Users\hi\Desktop\vs python\Restaurant - Week 2 Sales.csv")

        # Load Food and Customer Data
        df_foods = pd.read_csv(r"C:\Users\hi\Desktop\vs python\restaurant_foods.csv")
        # Rename the primary key in customers to match sales tables for clean merging
        df_customers = pd.read_csv(r"C:\Users\hi\Desktop\vs python\restaurant_customers.csv").rename(columns={'ID': 'Customer ID'})
        print("All four data sources loaded successfully.")
        return df_week1, df_week2, df_foods, df_customers
    except FileNotFoundError as e:
        print(f"Error: Required file not found. Please ensure all four CSVs are in the same directory.")
        print(f"Missing file likely: {e.filename}")


def combine_and_preprocess_sales(df_week1, df_week2):
    """
    Combines Week 1 and Week 2 sales, adding a 'Week' column to group, separate or label the data by week..
    """
    
    # Tag each DataFrame with its week number
    df_week1['Week'] = 1
    df_week2['Week'] = 2

    # Concatenate the two DataFrames into a single, unified sales record
    df_sales_combined = pd.concat([df_week1, df_week2], ignore_index=True)
    
    # Using numpy to count unique customers
    unique_customers = np.unique(df_sales_combined['Customer ID']).size
    total_orders = df_sales_combined.shape[0]
    
    print(f"  > Total Combined Orders: {total_orders}")
    print(f"  > Total Unique Customers Served: {unique_customers}\n")
    
    return df_sales_combined

# --- Analytical Functions ---

def calculate_revenue_and_master_df(df_sales, df_foods):
    """
    Merges sales data with food price data to calculate financial metrics.
    """
    print("--- 2. Revenue Calculation and Data Merging ---")
    
    # Merge sales records with food details (item name and price)
    df_master = pd.merge(df_sales, df_foods, on='Food ID', how='left')
    
    # Calculate Total Revenue (assuming quantity=1 per sales record)
    total_revenue = df_master['Price'].sum()
    
    # Calculate Average Order Value (AOV) using numpy.mean for numerical efficiency
    aov = np.mean(df_master['Price'])
    
    print(f"  > Gross Total Revenue: ${total_revenue:,.2f}")
    print(f"  > Average Order Value (AOV): ${aov:,.2f}\n")
    
    return df_master

def analyze_food_performance(df_master):
    """
    Groups the master data by Food Item to summarize total revenue and order volume.
    Highlights the top-performing items.
    """
    print("--- 3. Food Performance Analysis (Top Sellers) ---")
    
    # Group by Food Item and aggregate statistics: sum of revenue, count of orders
    food_summary = df_master.groupby('Food Item').agg(
        Total_Revenue=('Price', 'sum'),
        Order_Count=('Food Item', 'size')).reset_index()
    
    # Sort the summary by Total Revenue in descending order
    food_summary = food_summary.sort_values(by='Total_Revenue', ascending=False)
    
    print("Top 5 Food Items by Total Revenue:")
    # Using .to_string() for clean output without index
    print(food_summary[['Food Item', 'Total_Revenue', 'Order_Count']].head(5).to_string(index=False))
    print("\n")
    
    return food_summary

def analyze_customer_segmentation(df_master, df_customers):
    """
    Merges with customer demographics to analyze spending by segment (Gender, Occupation).
    """
    print("--- 4. Customer Segmentation Analysis ---")
    
    # Merge sales with customer demographic data
    df_analysis = pd.merge(df_master, df_customers, on='Customer ID', how='left')
    
    # Segment 1: Revenue by Gender
    revenue_by_gender = df_analysis.groupby('Gender')['Price'].sum().sort_values(ascending=False)
    print("Revenue Breakdown by Gender:")
    # Format as currency for professional output
    print(revenue_by_gender.map('${:,.2f}'.format).to_string())
    
    # Segment 2: Top Occupations by Order Count
    top_occupations = df_analysis.groupby('Occupation')['Food Item'].count().sort_values(ascending=False).head(5)
    print("\nTop 5 Occupations Driving Order Volume:")
    print(top_occupations.to_string())
    print("\n")

# --- Visualization ---

def plot_top_foods_revenue(food_summary):
    """
    Generates a clear bar plot of the top 5 food items by revenue using Matplotlib.
    The plot is saved to 'top_5_food_revenue.png'.
    """
    print("--- 5. Generating Visualization (top_5_food_revenue.png) ---")
    
    # Select the top 5 items for visualization
    top_5_foods = food_summary.head(5)
    
    # Create the figure and axes for the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the bar plot (using the basic plt.bar function)
    bars = ax.bar(
        top_5_foods['Food Item'], 
        top_5_foods['Total_Revenue'], 
        color=['#4A90E2', '#50E3C2', '#F5A623', '#BD10E0', '#7ED321'] # Custom colors
    )
    
    # Enhance visualization elements
    ax.set_title('Top 5 Food Items by Total Revenue (2-Week Period)', fontsize=16, fontweight='bold')
    ax.set_xlabel('Food Item', fontsize=12)
    ax.set_ylabel('Total Revenue ($)', fontsize=12)
    
    # Add revenue labels on top of the bars for precise reading
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 5, f'${yval:,.0f}', ha='center', va='bottom', fontsize=10)

    # Final styling and save
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('top_5_food_revenue.png')
    print("Plot successfully saved as 'top_5_food_revenue.png'.")
    
# --- Main Execution Block ---

def main_pipeline():
    """
    The master function orchestrating the entire data analysis workflow.
    """
    # Load all data files
    df_week1, df_week2, df_foods, df_customers = load_data()
    
    # 1. Combine Sales Data
    df_sales_combined = combine_and_preprocess_sales(df_week1, df_week2)
    
    # 2. Calculate Revenue and create the master sales data frame
    df_master = calculate_revenue_and_master_df(df_sales_combined, df_foods)
    
    # 3. Analyze Food Performance
    food_summary = analyze_food_performance(df_master)
    
    # 4. Analyze Customer Demographics
    analyze_customer_segmentation(df_master, df_customers)
    
    # 5. Visualize Results
    plot_top_foods_revenue(food_summary)


if __name__ == '__main__':
    main_pipeline()
