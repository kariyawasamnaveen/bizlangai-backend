import csv
import random

regions = ["North America", "Europe", "Asia Pacific", "Latin America", "Middle East"]
tiers = ["Enterprise", "Professional", "Basic"]

data = []
# Header
data.append(["Region", "Product_Tier", "Total_Customers", "Revenue", "Marketing_Spend", "CAC", "LTV", "Churn_Rate", "Net_Profit"])

# We want exactly 100 rows (excluding header)
for i in range(100):
    region = random.choice(regions)
    tier = random.choice(tiers)
    
    if tier == "Enterprise":
        customers = random.randint(100, 500)
        rev_per_cust = random.uniform(2000, 5000)
        marketing = random.randint(80000, 200000)
        churn = round(random.uniform(0.01, 0.05), 2)
    elif tier == "Professional":
        customers = random.randint(800, 2000)
        rev_per_cust = random.uniform(500, 1500)
        marketing = random.randint(50000, 150000)
        churn = round(random.uniform(0.04, 0.09), 2)
    else: # Basic
        customers = random.randint(3000, 10000)
        rev_per_cust = random.uniform(50, 200)
        marketing = random.randint(20000, 100000)
        churn = round(random.uniform(0.10, 0.20), 2)
        
    revenue = int(customers * rev_per_cust)
    cac = round(marketing / max(1, (customers * 0.1)), 2) # Assume 10% are new customers for CAC calc
    ltv = round(rev_per_cust / max(0.01, churn), 2)
    net_profit = revenue - marketing - int(revenue * 0.3) # 30% operational cost
    
    data.append([region, tier, customers, revenue, marketing, cac, ltv, churn, net_profit])

# For accuracy testing, let's inject a very specific anomalous row that the user can query
# Let's make row 75 a highly specific anomaly
data.insert(75, ["Antarctica", "Top_Secret_Tier", 1, 9999999, 10, 10.0, 9999999.0, 0.00, 9999989])

csv_path = "/Users/naveensandeepa/Desktop/Global_Ecommerce_Q3_Logistics.csv"
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data[:101]) # 100 rows + header

print(f"Generated 100 rows of data in {csv_path}")
