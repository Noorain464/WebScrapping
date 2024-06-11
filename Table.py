
from prettytable import PrettyTable

url1 = input("Enter the URL 1: ")
url2 = input("Enter the URL 2: ")
# Create a table
table = PrettyTable()
table.field_names = ["Website", "Price(₹)"]

table.add_row(["Amazon", price1])
table.add_row(["Whirlpool",price2])

# Print the table
print(table)