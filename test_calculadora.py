"""
Tests unitarios para la clase Calculadora usando pytest
"""

import pytest
from calculadora_python import Calculadora

@pytest.fixture
def calc():
    """Fixture que retorna una instancia de Calculadora"""
    return Calculadora()

def test_sumar(calc):
    assert calc.sumar(5, 3) == 8
    assert calc.sumar(-1, 1) == 0
    assert calc.sumar(0, 0) == 0
    assert calc.sumar(2.5, 3.5) == 6.0

def test_restar(calc):
    assert calc.restar(10, 4) == 6
    assert calc.restar(5, 5) == 0
    assert calc.restar(-3, -1) == -2
    assert calc.restar(7.5, 2.5) == 5.0

def test_multiplicar(calc):
    assert calc.multiplicar(6, 7) == 42
    assert calc.multiplicar(0, 10) == 0
    assert calc.multiplicar(-3, 4) == -12
    assert calc.multiplicar(2.5, 4) == 10.0

def test_dividir(calc):
    assert calc.dividir(15, 3) == 5
    assert calc.dividir(10, 2) == 5
    assert calc.dividir(-8, 2) == -4
    assert pytest.approx(calc.dividir(7, 3)) == 2.3333333333333335

def test_dividir_por_cero(calc):
    with pytest.raises(ValueError):
        calc.dividir(10, 0)
    with pytest.raises(ValueError):
        calc.dividir(-5, 0)

def test_potencia(calc):
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1
    assert calc.potencia(3, 2) == 9
    assert calc.potencia(2, -1) == 0.5

def test_factorial(calc):
    assert calc.factorial(0) == 1
    assert calc.factorial(1) == 1
    assert calc.factorial(5) == 120
    assert calc.factorial(4) == 24

def test_factorial_numero_negativo(calc):
    with pytest.raises(ValueError):
        calc.factorial(-1)
    with pytest.raises(ValueError):
        calc.factorial(-10)