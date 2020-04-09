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

