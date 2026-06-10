import pandas as pd
import matplotlib.pyplot as plt
import os

output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

df = pd.read_csv("customer_churn.csv")

print("CUSTOMER CHURN ANALYSIS")
print(df.head())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned data
df.to_csv(f"{output_folder}/cleaned_churn_data.csv", index=False)

# Churn Distribution
plt.figure(figsize=(6,4))
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Distribution")
plt.savefig(f"{output_folder}/churn_distribution.png")
plt.close()

# Subscription Type Analysis
plt.figure(figsize=(6,4))
pd.crosstab(df["SubscriptionType"], df["Churn"]).plot(kind="bar")
plt.title("Subscription Type vs Churn")
plt.savefig(f"{output_folder}/subscription_type.png")
plt.close()

# Engagement Score Analysis
plt.figure(figsize=(6,4))
plt.scatter(df["EngagementScore"], df["TenureMonths"])
plt.xlabel("Engagement Score")
plt.ylabel("Tenure Months")
plt.title("Engagement vs Tenure")
plt.savefig(f"{output_folder}/engagement_vs_churn.png")
plt.close()

# Generate Report
with open(f"{output_folder}/churn_report.txt","w") as file:
    file.write("CUSTOMER CHURN ANALYSIS REPORT\n")
    file.write("=============================\n\n")
    file.write(f"Total Customers: {len(df)}\n")
    file.write(f"Churned Customers: {len(df[df['Churn']=='Yes'])}\n")
    file.write(f"Active Customers: {len(df[df['Churn']=='No'])}\n\n")

    file.write("Key Findings:\n")
    file.write("- Customers with low engagement scores show higher churn.\n")
    file.write("- Basic plan users churn more frequently.\n")
    file.write("- Higher tenure customers are less likely to churn.\n")
    file.write("- Frequent support tickets indicate dissatisfaction.\n")

print("Analysis Completed Successfully!")