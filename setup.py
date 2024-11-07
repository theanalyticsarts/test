import pandas as pd
import numpy as np
import sqlite3
con = sqlite3.connect('db')
items = pd.read_csv("https://raw.githubusercontent.com/theanalyticsarts/test/refs/heads/main/items.csv")
sales = pd.read_csv("https://raw.githubusercontent.com/theanalyticsarts/test/refs/heads/main/sales.csv")

items.to_csv('items.csv', index=False)
sales.to_csv('sales.csv', index=False)

items.to_sql('items', index=False, con=con)
sales.to_sql('sales', index=False, con=con)

print("Done.")

