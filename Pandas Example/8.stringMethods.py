# -*- coding: utf-8 -*-

import pandas as pd

orders = pd.read_table('orders.tsv')

print(orders)
print(orders.columns)

print("****************************")

orders.item_name = orders.item_name.str.upper()
print(orders)

print("****************************")
#%%
print(orders.item_name.str.contains("Chicken".upper()))

print("****************************")
#%%
orders.choice_description = orders.choice_description.str.replace('[',' ').str.replace(']',' ')
print(orders)

print("****************************")