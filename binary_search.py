#Binary search

# Se divide la búsqueda a la mitad en cada iteración


# Vamos a encontrar la raíz cuadrada con este método

objetivo = int(input('Escoge un número: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2

print(f'La raíz cuadrada de {objetivo} es {respuesta}')