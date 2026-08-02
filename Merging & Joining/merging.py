import pandas as pd
#customer data
df_customer = pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "CustomerName": ["Ramesh", "Suresh", "Mahesh"],
})

#order data
df_order = pd.DataFrame({   
    "CustomerID": [1, 2, 4],
    "OrderAmount": [100, 200, 300],
})

#merging dataframes on index
df_merged = pd.merge(df_customer, df_order, on="CustomerID", how="inner")  # merges the two DataFrames on their index
#print("Inner Join:")
#print(df_merged)

df_merged_outer = pd.merge(df_customer, df_order, on="CustomerID", how="outer")  # merges the two DataFrames on their index
#print("\nOuter Join:")
#print(df_merged_outer)

df_merged_left = pd.merge(df_customer, df_order, on="CustomerID", how="left")  # merges the two DataFrames on their index
#print("\nLeft Join:")
#print(df_merged_left)

df_merged_right = pd.merge(df_customer, df_order, on="CustomerID", how="right")  # merges the two DataFrames on their index
#print("\nRight Join:")
#print(df_merged_right)

df_merged_cross = pd.merge(df_customer, df_order, on="CustomerID", how="cross")  # merges the two DataFrames on their index
print("\nCross Join:")
print(df_merged_cross)