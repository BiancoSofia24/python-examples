import csv
import os

div = "-----------------------------------------"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(ROOT_DIR, "file.csv")

def csv_to_rows(fname):
    with open(fname, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        if header != None:
            rows = [row for row in reader]
            return(rows)

rows = csv_to_rows(FILE_PATH)
print(".csv array2x2:")
print(rows)
print(div)

print("Array2x2 lenght:")
print(len(rows))
print(div)

toStr = "".join(map(str, rows))
print("Arrays:")
print(toStr)
print(div)

ids = ['0001', '0002']
values = ""
for i in range(len(rows)):
    string = "".join(map(str, rows[i])).split(sep=';')
    # print(string)
    element = string[0]
    for id in ids:
        if element == id:
            print(f"Element iteration: {i+1}")
            print(f"ID: {element} | Nombre: {string[1]}")
            values += f"[{element}, {string[1]}]"
            print(f"Extracted values array: {values}")

