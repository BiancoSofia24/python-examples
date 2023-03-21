import pandas
import requests
import statistics

url = f"https://api.recursospython.com/dollar"

req = requests.get(url, verify=False)
quotation = statistics.mean(req.json().values())
# quotation = 365
print("USD/ARS: ", quotation)

def usd_to_ars(usd):
    return usd * quotation

# First clean the Precio ARS column
excel_file = pandas.read_excel("file.xlsx")
print("Original file:")
print(excel_file)

excel_file["Precio ARS"] = excel_file["Precio USD"].apply(usd_to_ars)
excel_file.to_excel("file.xlsx", index=False)
print("Edited file:")
print(excel_file)

# # Requirements

# Requests
# ```python -m pip install requests```

# Pandas
# ```pip install pandas```

# Openpyxl
# ```pip install openpyxl```