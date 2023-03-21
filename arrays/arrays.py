array = [
    {'id_product': '0001', 'category': 'Category 1'}, 
    {'id_product': '0002', 'category': 'Category 2'}, 
    {'id_product': '0003', 'category': 'Category 3'}
]

print("EXTRACT VALUES FROM ARRAY")
print("-------------------------")

for i in range(len(array)):
    id_producto = array[i].get('id_product')
    category = array[i].get('category')
    print("ID:", id_producto, " Category:", category)

item = {'id_product': '2888', 'category': 'INTEGRAL DE COMERCIO', 'id_category': 25}
print("Object:",item)
print("Object lenght: ", len(item))

str = item.get("category")
print("Object value by key:", str)

date = array2 = "21/05/2021"
print("String date:", date)
print("String date array:",array2.split("/"))

print("Method 1")
print('String date without /: {f[2]}{f[1]}{f[0]}'.format(f=date.split("/")))

integer = int('{f[2]}{f[1]}{f[0]}'.format(f=date.split("/")))
print("Method 2")
print("Integer date without /:", integer)

string = '123.465,12'
print("String:", string)
print("String to array:", string.split("."))

new_string = string.split(".")
print("New string array lenght:",len(new_string))

string2 = ""
for i in range(len(new_string)):
    string2 += new_string[i]
print("String without .:",float(string2.replace(",", ".")))
