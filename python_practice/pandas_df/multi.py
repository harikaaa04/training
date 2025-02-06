import pandas as pd

data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'State': ['Delhi', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG', 'Odisha'],
    'Year': [2021, 2022, 2021, 2022, 2021, 2022],
    'Sales': [750000, 820000, 690000, 720000, 670000, 710000],
    'Profit': [95000, 102000, 85000, 91000, 77000, 88000]
}

df = pd.DataFrame(data)
df.set_index(["Region", "State", "Year"], inplace=True)

df_sales = pd.DataFrame({'State': ['Delhi', 'Tamil Nadu', 'West Bengal'], 'Sales': [200, 300, 400]})
df_profit = pd.DataFrame({'State': ['Delhi', 'Tamil Nadu', 'West Bengal'], 'Profit': [500, 430, 600]})

df_merged = pd.merge(df_sales, df_profit, on='State')
print(df_merged)
