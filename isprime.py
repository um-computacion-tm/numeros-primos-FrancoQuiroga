import unittest
import random
"Miller-Rabin prime function"
def is_prime(numero):
    if numero < 4:
        return True
    if numero % 2 == 0:
        return False
    es_primo = False
    cantdepruebas = 20
    for i in range(cantdepruebas):
        randomnum = random.randint(1,numero-1)
        if (randomnum ** (numero-1) % numero) != 1 % numero:
            es_primo = False
        else:
            es_primo = True
            
    return es_primo



class Testnumprimo(unittest.TestCase):
    def test_num1(self):
        resultado = is_prime(1)
        self.assertTrue(resultado)
    def test_num2(self):
        resultado = is_prime(2)
        self.assertTrue(resultado)
    def test_num3(self):
        resultado = is_prime(3)
        self.assertTrue(resultado)
    def test_num4(self):
        resultado = is_prime(4)
        self.assertFalse(resultado)
    def test_num8(self):
        resultado = is_prime(8)
        self.assertFalse(resultado)
    def test_num7(self):
        resultado = is_prime(7)
        self.assertTrue(resultado)

    def test_num97(self):
        resultado = is_prime(97)
        self.assertTrue(resultado)

    def test_num95(self):
        resultado = is_prime(95)
        self.assertFalse(resultado)

    def test_num6113(self):
        resultado = is_prime(6113)
        self.assertTrue(resultado)
    
    def test_num6114(self):
        resultado = is_prime(6114)
        self.assertFalse(resultado)

    def test_num6115(self):
        resultado = is_prime(6115)
        self.assertFalse(resultado)
        

unittest.main()
