# Reto #26: TESTING
# Publicación: 26/06/23 | MEDIA

#Crea tres test sobre el reto 12: "Viernes 13".
#- Puedes copiar una solución ya creada por otro usuario en el lenguaje que estés utilizando.
#- Debes emplear un mecanismo de ejecución de test que posea el lenguaje de programación que hayas seleccionado.
#- Los tres test deben de funcionar y comprobar diferentes situaciones (a tu elección).


# python -m unittest 26-testing.py -v
from datetime import datetime
import locale
import unittest

# Setea la variable LC_ALL al conjunto de código UTF-8 con descripción español España
locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')

def es_viernes_13(year: int, month: int) -> bool:
    if year < 0: raise ValueError('invalid year')
    if month < 0 or month > 12: ValueError('invalid month')
    d = datetime(year, month, 13)
    #Weekday as a number 0-6, 0 is Sunday
    return d.strftime("%w") == "5"

class TestViernes13(unittest.TestCase):

    def test_viernes_13_true(self):
        self.assertEqual(es_viernes_13(536, 4), True)

    def test_viernes_13_false(self):
        self.assertEqual(es_viernes_13(1, 1), False)

    def test_viernes_13_exception_year(self):
        with self.assertRaises(ValueError):
            es_viernes_13(-4444, 1)

    def test_viernes_13_exception_month(self):
        with self.assertRaises(ValueError):
            es_viernes_13(1978, -1)

if __name__ == '__main__':
    unittest.main()


