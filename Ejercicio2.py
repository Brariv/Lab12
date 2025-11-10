D = [1,2,3,4,5,6,7,8,9,10]

n = int(input("Ingrese el numero de la n potencia: "))
print("\n")

print("Numeros a evaluar:")
print(D)
print("\n")

D = list(map(lambda x: x**n, D))

print("Numeros elevados a la potencia", n, ":")
print(D)