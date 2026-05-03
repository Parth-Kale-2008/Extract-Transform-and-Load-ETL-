import pandas as pd

# Read file
data = pd.read_csv("py2.csv")

# Remove duplicate rows
data = data.drop_duplicates(subset=[
    'Transaction_ID',
    'Product_Brand',
    'Logistics_Partner',
    'Destination',
    'Quantity',
    'Unit_Price_USD',
    'Order_Date'
])

data['Transaction_ID'] = data['Transaction_ID'].astype(str).str.strip().str.upper() #str.upper() is used to make uppercase

data['Product_Brand'] = data['Product_Brand'].astype(str).str.strip().str.title() #str.strip() is used to remove unwanted space

data['Logistics_Partner'] = data['Logistics_Partner'].astype(str).str.strip().str.title() #str.title() converts in to title

data['Destination'] = data['Destination'].astype(str).str.strip().str.upper()
data['Quantity'] = pd.to_numeric(data['Quantity'], errors='coerce') #coerce is use to convert non numeric value to Nan

data['Unit_Price_USD'] = data['Unit_Price_USD'].astype(str).str.replace(',', '')

data['Unit_Price_USD'] = pd.to_numeric(data['Unit_Price_USD'], errors='coerce')
data['Order_Date'] = pd.to_datetime(data['Order_Date'], errors='coerce')
data = data.dropna() #dropna() is used to remove missing values 
data = data[data['Quantity'] > 0] # removes negitave quantities from the table 

data.to_csv("new_file.csv", index=False)
print("New CSV created successfully")
