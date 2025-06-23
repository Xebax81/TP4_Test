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
    assert calc.sumar(-2, 2) == 0
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

        
def test_modulo(calc):
    assert calc.modulo(10, 3) == 1
    assert calc.modulo(9, 3) == 0
    assert calc.modulo(-10, 3) == -10 % 3
    with pytest.raises(ValueError):
        calc.modulo(5, 0)

def test_promedio(calc):
    assert calc.promedio([1, 2, 3, 4, 5]) == 3
    assert calc.promedio([10]) == 10
    assert pytest.approx(calc.promedio([2.5, 3.5])) == 3.0
    with pytest.raises(ValueError):
        calc.promedio([])

def test_es_par(calc):
    assert calc.es_par(2) is True
    assert calc.es_par(3) is False
    assert calc.es_par(0) is True
    assert calc.es_par(-4) is True

def test_raiz_cuadrada(calc):
    assert calc.raiz_cuadrada(4) == 2
    assert calc.raiz_cuadrada(0) == 0
    assert pytest.approx(calc.raiz_cuadrada(2)) == 1.414213562
    with pytest.raises(ValueError):
        calc.raiz_cuadrada(-9)

def test_valor_absoluto(calc):
    assert calc.valor_absoluto(5) == 5
    assert calc.valor_absoluto(-5) == 5
    assert calc.valor_absoluto(0) == 0

def test_redondear(calc):
    assert calc.redondear(3.14159, 2) == 3.14
    assert calc.redondear(3.1459, 3) == 3.146
    assert calc.redondear(2.5, 0) == 2.0
    with pytest.raises(ValueError):
        calc.redondear("abc", 2)