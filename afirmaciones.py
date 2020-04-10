# Comprobar si se cumple o no, y si seguir con el programa o no

# Funciona
texto = 'Hola'

assert type(texto) == str, 'No es un string'

# Da error

texto = 2

assert type(texto) == str, str(texto) + ' no es un string'