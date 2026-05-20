import csv
import random
from datetime import datetime, timedelta

def generate_advanced_csv():
    regions = ["North America", "Europe", "Asia Pacific", "Latin America", "Middle East"]
    channels = ["B2B Direct", "E-commerce", "Retail Partners"]
    categories = ["Enterprise Software", "Cloud Infrastructure", "Hardware Systems", "Consulting Services"]

    data = []
    # Header
    data.append([
        "Transaction_Date", 
        "Region", 
        "Sales_Channel", 
        "Product_Category", 
        "Units_Sold", 
        "Revenue_USD", 
        "Marketing_Spend_USD", 
        "Operational_Cost_USD", 
        "Net_Profit_USD", 
        "CSAT_Score"
    ])

    start_date = datetime(2024, 1, 1)

    for i in range(500):
        # Random date within the year 2024
        days_to_add = random.randint(0, 364)
        t_date = start_date + timedelta(days=days_to_add)
        
        region = random.choice(regions)
        channel = random.choice(channels)
        category = random.choice(categories)
        
        # Base metrics depending on category
        if category == "Enterprise Software":
            units = random.randint(1, 50)
            price = random.uniform(5000, 15000)
            margin = 0.8
        elif category == "Cloud Infrastructure":
            units = random.randint(100, 5000)
            price = random.uniform(50, 200)
            margin = 0.6
        elif category == "Hardware Systems":
            units = random.randint(10, 200)
            price = random.uniform(1000, 5000)
            margin = 0.3
        else: # Consulting
            units = random.randint(1, 20)
            price = random.uniform(10000, 25000)
            margin = 0.5
            
        revenue = round(units * price, 2)
        
        # Marketing spend is 5% to 15% of revenue
        marketing = round(revenue * random.uniform(0.05, 0.15), 2)
        
        # Operational cost depends on margin
        op_cost = round(revenue * (1 - margin), 2)
        
        # Add some random variability to costs
        marketing += random.uniform(-1000, 1000)
        op_cost += random.uniform(-5000, 5000)
        
        marketing = max(100, marketing)
        op_cost = max(100, op_cost)
        
        net_profit = round(revenue - marketing - op_cost, 2)
        
        # CSAT score out of 10.0
        csat = round(random.uniform(6.5, 9.9), 1)
        
        data.append([
            t_date.strftime("%Y-%m-%d"),
            region,
            channel,
            category,
            units,
            revenue,
            marketing,
            op_cost,
            net_profit,
            csat
        ])

    csv_path = "/Users/naveensandeepa/Desktop/Global_Ecommerce_Q3_Logistics.csv"
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Generated 500 rows of advanced data in {csv_path}")

if __name__ == "__main__":
    generate_advanced_csv()
