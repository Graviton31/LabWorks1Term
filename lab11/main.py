import requests, csv
from io import TextIOWrapper, BytesIO
import pandas as pd

# task 1
url_users = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url_users)
users = response.json()

print("Список пользователей (имя, город, телефон):\n" + "-"*50)
for user in users:
    name = user["name"]
    city = user["address"]["city"]
    phone = user["phone"]
    print(f"Имя: {name:30} | Город: {city:15} | Телефон: {phone}")

# task 2
csv_url = "https://www.stats.govt.nz/assets/Uploads/Rental-price-indexes/Rental-price-indexes-September-2023/Download-data/rental-price-indexes-september-2023.csv"

resp = requests.get(csv_url)
resp.raise_for_status()
csv_content = TextIOWrapper(BytesIO(resp.content), encoding='utf-8')

print("\nЧтение CSV (способ 1 — csv.reader):\n" + "-"*50)
reader = csv.reader(csv_content)
for i, row in enumerate(reader):
    if i < 5: 
        print(row)

df = pd.read_csv(csv_url)
print("\nЧтение CSV (способ 2 — pandas):\n" + "-"*50)
print(df.head()) 