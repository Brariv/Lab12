D = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']

To_Delete = ['amarillo', 'cafe', 'blanco']

D = list(filter(lambda x: x not in To_Delete, D))

print("Lista original:")
print(['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro'])
print("\n")

print("Lista de elementos a eliminar:")
print(To_Delete)
print("\n")

print("Lista después de eliminar elementos:")
print(D)