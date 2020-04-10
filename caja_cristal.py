import unittest
import recursividad

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20
        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_edad(self):
        edad = 17
        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)

    def test_recursividad(self):
        num = 2
        resultado = recursividad.factorial(num)

        self.assertEqual(resultado, 2)

if __name__ == '__main__':
    unittest.main()