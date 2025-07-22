# In this file, we create the customer cohorts by customer lifetime value.

import pandas as pd


# ---- 1. Load your order data (one row per order) ----

df = pd.read_csv("/datasets/Orders.csv", delimiter=';')  # Update the filename
df = df.rename(columns=lambda x: x.strip().replace(' ', ''))

# ---- 2. Calculate CLV per customer ----
df_clv = df.groupby('CustomerID', as_index=False)['Profit'].sum()

# We define customer lifetime value as profit per customer brings.


# ---- 3. Calculate percentile rank ----

df_clv['CLV Percentile'] = df_clv['Profit'].rank(pct=True, ascending=True)

# In order to define the cohort, we calculate the percentile firstly.

# ---- 4. Assign custom cohort ----


def cohort(percentile):
    if percentile >= 0.95:
        return "Top 5%"
    elif percentile >= 0.80:
        return "Next 15%"
    elif percentile >= 0.50:
        return "Next 30%"
    else:
        return "Bottom 50%"
# The more profit a customer contributes, the topper percentile it sits in.


df_clv['CLV Cohort'] = df_clv['CLV Percentile'].apply(cohort)
df_clv.rename(columns={"CustomerID": "Customer ID"}, inplace=True)

print(df_clv.head(5))

# ---- 5. Save to CSV for Tableau ----
df_clv.to_csv("Customer_cohorts.csv", index=False)

# The new file 'Customer_cohorts.csv' is created. We import it and build the relationship with other tables in Tableau.
