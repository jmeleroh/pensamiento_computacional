#Tuplas
"""
Son listas inmutables de objetos

"""

my_tuple = (1,'dos', 'tres')

print(my_tuple[0])

#Rangos

"""
Secuencia de enteros inmutables
range(comienzo,fin,pasos)
"""
comienzo = 0
fin = 100
pasos = 2
my_range = range(comienzo, fin, pasos)

for i in my_range:
    print(i)

#Listas y mutabilidad

my_list = []

my_list.append(1)

my_list.pop(0)

for i in my_list:
    print(i)

# Clonar listas    

clone_list = list(my_list)
clone2_list = my_list[::]
print(id(my_list), id(clone_list), id(clone2_list))

# List comprehension
"""
append(x): Agrega un item al final de la lista.
extend(iterable): extiende la lista añadiendo todos los items desde el iterable
insert(i,x): Inserta un item en la posición i
remove(x): Elimina el primer item de la lista que tenga el valor de x, plantea un Value Error si no encuentra el valor
pop([i]): Elmina el item en la posición dada en la lista y lo retorna, si no tiene item elimina el ultimo.
clear(): Elimina todos los items de la lista
index(x[, start, [, end]]): Retorna la lista de items cuyo valor es igual a x o el slice aplicado como opcional.
count(x): Retorna el número de veces que x aparece en la lista
sort(key=None, reverse=False): Ordena los items de la lista en su lugar
reverse(): Invierte los valores de la lista en su lugar
copy(): Retorna una copia superficial de la lista.
"""
# Diccionarios

"""
Son como listas, pero en vez de utilizar índices usa claves
"""

diccionario = {
    'Juan': 35,
    'Erica': 30,
    'Pepe': 47,
}

print(diccionario.get('José', 32))  #Busca a José, si no existe devuelve 32
# values() o keys()
for edades in diccionario.values():
    print(edades)