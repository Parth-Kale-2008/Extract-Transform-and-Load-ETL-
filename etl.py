import pandas as pd

data = pd.read_csv("py.csv")
print("this is the orignal data")
print(data)

data = data.drop_duplicates()
data = data.dropna(subset=['date','product','quantity','price'])
data['product'] = data['product'].str.strip().str.title()
data['city'] = data['city'].str.strip().str.title()

data['date'] = pd.to_datetime(data['date'], errors='coerce')
data['quantity'] = pd.to_numeric(data['quantity'],errors='coerce')
data['price'] = data['price'].astype(str).str.replace(',', '')
data['price'] = pd.to_numeric(data['price'], errors='coerce')

data = data.dropna()
data = data[data['quantity']>0]
data['total'] = data['quantity'] * data['price']
data.to_csv("cleaned_sales.csv", index=False)

print(data)
