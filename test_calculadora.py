"""
Tests unitarios para la clase Calculadora
"""

import unittest
from calculadora_python import Calculadora

class TestCalculadora(unittest.TestCase):
    """Clase de tests para la calculadora"""
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.calc = Calculadora()
    
    def test_sumar(self):
        """Test para la función sumar"""
        self.assertEqual(self.calc.sumar(5, 3), 8)
        self.assertEqual(self.calc.sumar(-1, 1), 0)
        self.assertEqual(self.calc.sumar(0, 0), 0)
        self.assertEqual(self.calc.sumar(2.5, 3.5), 6.0)
    
    def test_restar(self):
        """Test para la función restar"""
        self.assertEqual(self.calc.restar(10, 4), 6)
        self.assertEqual(self.calc.restar(5, 5), 0)
        self.assertEqual(self.calc.restar(-3, -1), -2)
        self.assertEqual(self.calc.restar(7.5, 2.5), 5.0)
    
    def test_multiplicar(self):
        """Test para la función multiplicar"""
        self.assertEqual(self.calc.multiplicar(6, 7), 42)
        self.assertEqual(self.calc.multiplicar(0, 10), 0)
        self.assertEqual(self.calc.multiplicar(-3, 4), -12)
        self.assertEqual(self.calc.multiplicar(2.5, 4), 10.0)
    
    def test_dividir(self):
        """Test para la función dividir"""
        self.assertEqual(self.calc.dividir(15, 3), 5)
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(-8, 2), -4)
        self.assertAlmostEqual(self.calc.dividir(7, 3), 2.3333333333333335)
    
    def test_dividir_por_cero(self):
        """Test para verificar que la división por cero lanza excepción"""
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)
        
        with self.assertRaises(ValueError):
            self.calc.dividir(-5, 0)
    
    def test_potencia(self):
        """Test para la función potencia"""
        self.assertEqual(self.calc.potencia(2, 3), 8)
        self.assertEqual(self.calc.potencia(5, 0), 1)
        self.assertEqual(self.calc.potencia(3, 2), 9)
        self.assertEqual(self.calc.potencia(2, -1), 0.5)
    
    def test_factorial(self):
        """Test para la función factorial"""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(4), 24)
    
    def test_factorial_numero_negativo(self):
        """Test para verificar que el factorial de números negativos lanza excepción"""
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)
        
        with self.assertRaises(ValueError):
            self.calc.factorial(-10)

if __name__ == '__main__':
    # Ejecutar los tests con verbosidad
    unittest.main(verbosity=2)