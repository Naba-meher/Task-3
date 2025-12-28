import pandas as pd

# Step 1: Load dataset
df = pd.read_csv("sales_data.csv")

# Step 2: Handle missing values
df = df.dropna().drop_duplicates()

# Step 3: Calculate metrics
df["Sales"] = df["Quantity"] * df["Price"]
total_sales = df["Sales"].sum()
best_product = df.groupby("Product")["Sales"].sum().idxmax()
best_product_sales = df.groupby("Product")["Sales"].sum().max()
average_sales = df["Sales"].mean()

# Step 4: Report
print("📊 Sales Report")
print("---------------------------")
print(f"💰 Total Sales: ₹{total_sales:,.2f}")
print(f"🏆 Best-Selling Product: {best_product} (₹{best_product_sales:,.2f})")
print(f"📈 Average Sales per Transaction: ₹{average_sales:,.2f}")
