D = [
    {'Make' : 'Nokia', 'Model' : 216, 'Color' : 'Black'},
    {'Make' : 'Apple', 'Model' : 2, 'Color' : 'Silver'},
    {'Make' : 'Huawei', 'Model' : 50, 'Color' : 'Gold'},
    {'Make' : 'Samsung', 'Model' : 7, 'Color' : 'Blue'},
]

print("Diccionario original:")
for d in D:
    print(d)
print("\n")

D1 = sorted(D, key=lambda x: x['Make'])
print("Diccionario ordenado por Make:")
for d in D1:
    print(d)
print("\n")

D2 = sorted(D, key=lambda x: x['Model'])
print("Diccionario ordenado por Model:")
for d in D2:
    print(d)
print("\n")

D3 = sorted(D, key=lambda x: x['Color'])
print("Diccionario ordenado por Color:")
for d in D3:
    print(d)
print("\n")