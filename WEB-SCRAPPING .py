from bs4 import BeautifulSoup
import requests

url1 = input("Enter the URL 1: ")
url2 = input("Enter the URL 2: ")

headers = ({'User-Agent':"https://explore.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes",'Accept-Language':'en-US,en:q=0.5'})
result1 = requests.get(url1,headers=headers)
soup1 = BeautifulSoup(result1.content,"html.parser")
#soup1 = BeautifulSoup(soup.prettify(),"html.parser")
title1 = soup1.find(id='productTitle').get_text()
price1 = soup1.find('span',{"class":'a-price-whole'}).text.strip()
print(title1)
print(price1)

result2 = requests.get(url2,headers=headers)
soup2 = BeautifulSoup(result2.content,"html.parser")
#soup1 = BeautifulSoup(soup.prettify(),"html.parser")
title2 = soup2.find('h1',{"class":'vtex-store-components-3-x-productNameContainer vtex-store-components-3-x-productNameContainer--quickview mv0 t-heading-4'}).text.strip()
price2 = soup2.find('span',{"class":'vtex-product-price-1-x-spotPrice'}).text.strip()
print(title2)
print(price2)

from prettytable import PrettyTable

# Create a table
table = PrettyTable()
table.field_names = ["Website", "Price(₹)"]

table.add_row(["Amazon", price1])
table.add_row(["Whirlpool",price2])

# Print the table
print(table)