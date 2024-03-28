import unittest
def is_prime(numero):
    numerocheck = 9
    result = False
    if 0 < numero < 4:
        result = True
        return result
    while numerocheck > 0:
        divisioncheck = numero % numerocheck
        if (numero % 2) == 0:
            return False
        if divisioncheck == 0:
            result = False
        else:
            return True
        numerocheck = numerocheck - 1
    return result
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
