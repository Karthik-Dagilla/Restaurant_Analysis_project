# 🍽️ Restaurant Analysis Project

A data-analysis project focused on understanding restaurant sales trends, customer behavior, and food item performance using Python. This project includes data cleaning, merging, KPI calculation, quality checks, and visualizations that support business decision-making.

---

## Objective  
To analyze restaurant sales, customer data, and food performance trends to derive insights that can guide operational decisions and improve revenue.

---

## Dataset Description  
This project uses four dataset files:

- Restaurant – Week 1 Sales.xls  
- Restaurant – Week 2 Sales.xls  
- restaurant_customers.xls  
- restaurant_foods.xls  

The datasets contain:

- Order information  
- Food items & categories  
- Customer details  
- Daily/weekly order timestamps  
- Quantity & revenue details  

---

# Standard Operating Procedures (SOPs)

### **1. Data Cleaning SOP**
- Remove duplicate records.  
- Convert date columns into a consistent format.  
- Ensure all missing values are handled using valid logic.  
- Validate data types using:
  - `df.info()`
  - `df.describe()`
  - `df.isnull().sum()`

---

### **2. Classification & Labeling SOP**
- Categorize food items according to predefined item categories.  
- Mark unclear items under "Miscellaneous” and review separately.  
- Classify customers based on:
  - Frequent: >3 orders  
  - Moderate: 2–3 orders  
  - One-time: 1 order  

---

### **3. Quality Check SOP**
- Recalculate KPIs twice to verify accuracy.  
- Maintain an error log for anomalies such as:  
  - missing categories  
  - wrong dates  
  - duplicate orders  
- Document major issues and corrections in a mini quality report.

---

### **4. Reporting & Visualization SOP**
- Use clear chart titles and axis labels.  
- Maintain a simple and consistent color theme.  
- Add 2–3 lines of insight below each chart.  
- Ensure each visualization reflects accurate aggregations (sum, mean, groupby).  

---

## Analysis Performed
- Loaded and merged four related restaurant datasets.  
- Calculated KPIs:
  - Total revenue  
  - Average order value  
  - Orders per customer  
  - Quantity sold per item  
- Identified top-performing food items.  
- Performed customer segmentation.  
- Conducted time-series analysis:
  - Week-wise comparison  
  - Daily sales patterns  

---

## Key Insights (Replace with your actual results)
1. Steak is the highest revenue-generating item
   Steak generated $1,250, making it the top-performing menu item.

2. Pasta shows strong performance
   Pasta brought in $755, making it the second-highest revenue generator.

3. Burrito and Salad are mid-performing items
   Burrito revenue: $569
   Salad revenue: $540
   Both show steady demand but lower revenue compared to top items.

4. Quesadilla is the lowest revenue item
   Quesadilla generated only $208, indicating very low demand.

5. Large revenue gap between items
   Steak earns 6x more revenue than Quesadilla, showing strong customer preference for premium dishes.
---

##  Tools Used
- Python  
- Pandas  
- NumPy  
- Matplotlib 
- Jupyter Notebook  

---

## Conclusion
This project highlights skills in data cleaning, merging, analysis, visualization, and SOP-driven workflow. Insights from the project support operational improvements such as identifying top food items, customer behavior patterns, and revenue opportunities.

---

## Author  
**Karthik Dagilla**  
GitHub: github.com/Karthik-Dagilla  
LinkedIn: linkedin.com/in/karthik-dagilla
