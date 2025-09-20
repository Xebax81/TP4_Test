"""
Pruebas de Regresión para la Calculadora
Estas pruebas aseguran que las funcionalidades existentes no se rompan con nuevos cambios
"""

import pytest
import math
from calculadora_python import Calculadora


@pytest.fixture
def calc():
    """Fixture para crear una instancia de calculadora"""
    return Calculadora()


@pytest.mark.regression
class TestRegresionOperacionesCore:
    """Pruebas de regresión para operaciones fundamentales"""

    def test_regresion_operaciones_basicas_valores_conocidos(self, calc):
        """Test de regresión con valores conocidos que no deben cambiar nunca"""
        # Estos valores son fundamentales y NUNCA deben cambiar
        assert calc.sumar(2, 2) == 4
        assert calc.restar(5, 3) == 2
        assert calc.multiplicar(3, 4) == 12
        assert calc.dividir(10, 2) == 5

    def test_regresion_operaciones_con_cero(self, calc):
        """Test de regresión para operaciones con cero"""
        # Comportamiento crítico que no debe cambiar
        assert calc.sumar(0, 5) == 5
        assert calc.sumar(5, 0) == 5
        assert calc.restar(5, 0) == 5
        assert calc.restar(0, 5) == -5
        assert calc.multiplicar(0, 100) == 0
        assert calc.multiplicar(100, 0) == 0

    def test_regresion_division_por_cero(self, calc):
        """Test de regresión para división por cero - debe mantener el error"""
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            calc.dividir(5, 0)
        
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            calc.dividir(0, 0)

    def test_regresion_numeros_negativos(self, calc):
        """Test de regresión para operaciones con números negativos"""
        assert calc.sumar(-2, -3) == -5
        assert calc.sumar(-2, 3) == 1
        assert calc.restar(-5, -3) == -2
        assert calc.multiplicar(-2, 3) == -6
        assert calc.multiplicar(-2, -3) == 6
        assert calc.dividir(-10, 2) == -5
        assert calc.dividir(-10, -2) == 5


@pytest.mark.regression
class TestRegresionOperacionesAvanzadas:
    """Pruebas de regresión para operaciones avanzadas"""

    def test_regresion_potencia_casos_especiales(self, calc):
        """Test de regresión para casos especiales de potencia"""
        # Casos que no deben cambiar nunca
        assert calc.potencia(2, 0) == 1  # Cualquier número a la 0 = 1
        assert calc.potencia(0, 5) == 0  # 0 a cualquier potencia positiva = 0
        assert calc.potencia(1, 100) == 1  # 1 a cualquier potencia = 1
        assert calc.potencia(2, 3) == 8
        assert calc.potencia(5, 2) == 25

    def test_regresion_factorial_valores_conocidos(self, calc):
        """Test de regresión para factoriales con valores conocidos"""
        # Valores de factorial que NUNCA deben cambiar
        assert calc.factorial(0) == 1
        assert calc.factorial(1) == 1
        assert calc.factorial(2) == 2
        assert calc.factorial(3) == 6
        assert calc.factorial(4) == 24
        assert calc.factorial(5) == 120
        assert calc.factorial(6) == 720

    def test_regresion_factorial_numeros_negativos(self, calc):
        """Test de regresión para factorial con números negativos"""
        with pytest.raises(ValueError, match="El factorial no está definido para números negativos"):
            calc.factorial(-1)
        
        with pytest.raises(ValueError, match="El factorial no está definido para números negativos"):
            calc.factorial(-10)

    def test_regresion_modulo(self, calc):
        """Test de regresión para operación módulo"""
        assert calc.modulo(10, 3) == 1
        assert calc.modulo(15, 4) == 3
        assert calc.modulo(20, 5) == 0
        assert calc.modulo(7, 7) == 0
        
        # Módulo por cero debe fallar
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            calc.modulo(5, 0)


@pytest.mark.regression
class TestRegresionFuncionesEspeciales:
    """Pruebas de regresión para funciones especiales"""

    def test_regresion_raiz_cuadrada(self, calc):
        """Test de regresión para raíz cuadrada"""
        assert calc.raiz_cuadrada(0) == 0
        assert calc.raiz_cuadrada(1) == 1
        assert calc.raiz_cuadrada(4) == 2
        assert calc.raiz_cuadrada(9) == 3
        assert calc.raiz_cuadrada(16) == 4
        assert calc.raiz_cuadrada(25) == 5

        # Números negativos deben fallar
        with pytest.raises(ValueError, match="No se puede calcular la raíz cuadrada de un número negativo"):
            calc.raiz_cuadrada(-1)

    def test_regresion_valor_absoluto(self, calc):
        """Test de regresión para valor absoluto"""
        assert calc.valor_absoluto(5) == 5
        assert calc.valor_absoluto(-5) == 5
        assert calc.valor_absoluto(0) == 0
        assert calc.valor_absoluto(-10.5) == 10.5
        assert calc.valor_absoluto(10.5) == 10.5

    def test_regresion_es_par(self, calc):
        """Test de regresión para función es_par"""
        # Números pares
        assert calc.es_par(0) is True
        assert calc.es_par(2) is True
        assert calc.es_par(4) is True
        assert calc.es_par(-2) is True
        assert calc.es_par(-4) is True

        # Números impares
        assert calc.es_par(1) is False
        assert calc.es_par(3) is False
        assert calc.es_par(5) is False
        assert calc.es_par(-1) is False
        assert calc.es_par(-3) is False

    def test_regresion_redondear(self, calc):
        """Test de regresión para función redondear"""
        assert calc.redondear(3.14159, 2) == 3.14
        assert calc.redondear(3.14159, 3) == 3.142
        assert calc.redondear(3.14159, 0) == 3.0
        assert calc.redondear(2.5, 0) == 2.0  # Comportamiento específico de round()

        # Parámetros inválidos deben fallar
        with pytest.raises(ValueError):
            calc.redondear("abc", 2)


@pytest.mark.regression
class TestRegresionFuncionesLista:
    """Pruebas de regresión para funciones que operan con listas"""

    def test_regresion_promedio(self, calc):
        """Test de regresión para cálculo de promedio"""
        assert calc.promedio([1, 2, 3, 4, 5]) == 3
        assert calc.promedio([10]) == 10
        assert calc.promedio([0, 0, 0]) == 0
        assert calc.promedio([-1, 1]) == 0

        # Lista vacía debe fallar
        with pytest.raises(ValueError, match="La lista no puede estar vacía"):
            calc.promedio([])

    def test_regresion_maximo_minimo(self, calc):
        """Test de regresión para máximo y mínimo"""
        numeros = [1, 5, 3, 9, 2, 7]
        
        assert calc.maximo(numeros) == 9
        assert calc.minimo(numeros) == 1
        
        # Un solo elemento
        assert calc.maximo([42]) == 42
        assert calc.minimo([42]) == 42
        
        # Números negativos
        negativos = [-5, -1, -10, -3]
        assert calc.maximo(negativos) == -1
        assert calc.minimo(negativos) == -10

        # Listas vacías deben fallar
        with pytest.raises(ValueError, match="La lista no puede estar vacía"):
            calc.maximo([])
        
        with pytest.raises(ValueError, match="La lista no puede estar vacía"):
            calc.minimo([])


@pytest.mark.regression
class TestRegresionFuncionesTrigonometricas:
    """Pruebas de regresión para funciones trigonométricas y logarítmicas"""

    def test_regresion_seno_valores_conocidos(self, calc):
        """Test de regresión para seno con valores conocidos"""
        # Valores que deben mantenerse constantes
        assert abs(calc.seno(0) - 0) < 0.0001
        assert abs(calc.seno(math.pi/2) - 1) < 0.0001
        assert abs(calc.seno(math.pi) - 0) < 0.0001
        assert abs(calc.seno(3*math.pi/2) - (-1)) < 0.0001

    def test_regresion_logaritmo(self, calc):
        """Test de regresión para logaritmo base 10"""
        assert abs(calc.logaritmo(1) - 0) < 0.0001
        assert abs(calc.logaritmo(10) - 1) < 0.0001
        assert abs(calc.logaritmo(100) - 2) < 0.0001
        assert abs(calc.logaritmo(1000) - 3) < 0.0001

        # Números no positivos deben fallar
        with pytest.raises(ValueError, match="El logaritmo solo está definido para números positivos"):
            calc.logaritmo(0)
        
        with pytest.raises(ValueError, match="El logaritmo solo está definido para números positivos"):
            calc.logaritmo(-1)


@pytest.mark.regression
class TestRegresionComportamientoSistema:
    """Pruebas de regresión para comportamiento general del sistema"""

    def test_regresion_manejo_tipos_datos(self, calc):
        """Test de regresión para manejo de tipos de datos"""
        # Enteros y flotantes deben funcionar igual
        assert calc.sumar(2, 3.0) == 5.0
        assert calc.sumar(2.0, 3) == 5.0
        assert calc.multiplicar(2, 3.5) == 7.0

    def test_regresion_precision_decimales(self, calc):
        """Test de regresión para precisión con decimales"""
        # Casos conocidos que pueden tener problemas de precisión flotante
        resultado = calc.sumar(0.1, 0.2)
        assert abs(resultado - 0.3) < 0.0001

        resultado = calc.dividir(1, 3)
        assert abs(resultado - 0.3333333333333333) < 0.0001

    def test_regresion_encadenamiento_operaciones(self, calc):
        """Test de regresión para encadenamiento de operaciones"""
        # Test de workflow que no debe cambiar
        resultado = calc.sumar(2, 3)          # 5
        resultado = calc.multiplicar(resultado, 2)  # 10
        resultado = calc.restar(resultado, 3)      # 7
        resultado = calc.dividir(resultado, 2)     # 3.5
        
        assert resultado == 3.5

    def test_regresion_estados_calculadora(self, calc):
        """Test de regresión para verificar que la calculadora no mantiene estado"""
        # Cada operación debe ser independiente
        calc.sumar(100, 200)  # Esta operación no debe afectar las siguientes
        assert calc.sumar(2, 3) == 5
        
        calc.dividir(1000, 10)  # Esta tampoco
        assert calc.multiplicar(4, 5) == 20


@pytest.mark.regression
@pytest.mark.critical
class TestRegresionCriticos:
    """Pruebas de regresión críticas - estas NUNCA deben fallar"""

    def test_regresion_operaciones_basicas_inmutables(self, calc):
        """Test de operaciones que son inmutables matemáticamente"""
        # Estos son axiomas matemáticos que NUNCA pueden cambiar
        assert calc.sumar(0, 0) == 0
        assert calc.multiplicar(1, 1) == 1
        assert calc.restar(5, 5) == 0
        assert calc.dividir(1, 1) == 1
        assert calc.potencia(1, 1000000) == 1
        assert calc.valor_absoluto(0) == 0

    def test_regresion_consistencia_matematica(self, calc):
        """Test de consistencia matemática que debe mantenerse"""
        # Propiedades conmutativas
        assert calc.sumar(3, 5) == calc.sumar(5, 3)
        assert calc.multiplicar(3, 5) == calc.multiplicar(5, 3)
        
        # Elementos neutros
        assert calc.sumar(7, 0) == 7
        assert calc.multiplicar(7, 1) == 7
        
        # Inversos
        assert calc.sumar(5, -5) == 0
        assert calc.dividir(5, 5) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-m", "regression"])