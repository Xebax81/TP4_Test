"""
Pruebas de Integración para la Calculadora
Estas pruebas verifican que los componentes trabajen correctamente juntos
"""

import pytest
import math
from calculadora_python import Calculadora


@pytest.fixture
def calc():
    """Fixture para crear una instancia de calculadora"""
    return Calculadora()


class TestIntegracionOperacionesBasicas:
    """Pruebas de integración para operaciones básicas"""

    def test_operaciones_combinadas(self, calc):
        """Test de operaciones matemáticas combinadas"""
        # Caso: (2 + 3) * 4 = 20
        resultado_suma = calc.sumar(2, 3)
        resultado_final = calc.multiplicar(resultado_suma, 4)
        assert resultado_final == 20

    def test_cadena_operaciones_complejas(self, calc):
        """Test de cadena de operaciones complejas"""
        # Caso: ((10 - 2) / 2) ^ 2 = 16
        resultado_resta = calc.restar(10, 2)
        resultado_division = calc.dividir(resultado_resta, 2)
        resultado_final = calc.potencia(resultado_division, 2)
        assert resultado_final == 16

    def test_workflow_calculo_promedio_con_operaciones(self, calc):
        """Test de workflow completo: calcular promedio y aplicar operaciones"""
        numeros = [2, 4, 6, 8, 10]
        promedio = calc.promedio(numeros)
        assert promedio == 6

        # Aplicar operaciones al promedio
        resultado_potencia = calc.potencia(promedio, 2)
        assert resultado_potencia == 36

        resultado_raiz = calc.raiz_cuadrada(resultado_potencia)
        assert resultado_raiz == 6


class TestIntegracionManejErrores:
    """Pruebas de integración para manejo de errores"""

    def test_cadena_operaciones_con_errores(self, calc):
        """Test de manejo de errores en cadena de operaciones"""
        # Operación válida seguida de error
        resultado_valido = calc.sumar(10, 5)
        assert resultado_valido == 15

        # Intentar dividir por cero
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            calc.dividir(resultado_valido, 0)

        # Verificar que el calculador sigue funcionando después del error
        resultado_posterior = calc.multiplicar(resultado_valido, 2)
        assert resultado_posterior == 30

    def test_recuperacion_despues_error(self, calc):
        """Test de recuperación después de errores"""
        # Generar error
        with pytest.raises(ValueError):
            calc.factorial(-5)

        # Verificar que la calculadora sigue funcionando
        assert calc.sumar(1, 1) == 2
        assert calc.multiplicar(3, 3) == 9


class TestIntegracionEstadisticas:
    """Pruebas de integración para funciones estadísticas"""

    def test_workflow_analisis_estadistico(self, calc):
        """Test de workflow completo de análisis estadístico"""
        datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Calcular estadísticas básicas
        promedio = calc.promedio(datos)
        assert promedio == 5.5

        maximo = calc.maximo(datos)
        assert maximo == 10

        minimo = calc.minimo(datos)
        assert minimo == 1

        # Operaciones derivadas
        rango = calc.restar(maximo, minimo)
        assert rango == 9

    def test_integracion_operaciones_matematicas_avanzadas(self, calc):
        """Test de integración de operaciones matemáticas avanzadas"""
        numero = 100

        # Logaritmo y exponencial (verificar que son operaciones inversas)
        log_resultado = calc.logaritmo(numero)
        exp_resultado = calc.potencia(10, log_resultado)
        assert abs(exp_resultado - numero) < 0.0001  # Tolerancia para flotantes

        # Operaciones trigonométricas
        angulo = math.pi / 2  # 90 grados en radianes
        seno = calc.seno(angulo)
        assert abs(seno - 1.0) < 0.0001


class TestIntegracionRobustez:
    """Pruebas de integración para robustez del sistema"""

    def test_operaciones_con_numeros_grandes(self, calc):
        """Test con números grandes"""
        numero_grande = 999999999
        resultado_suma = calc.sumar(numero_grande, 1)
        assert resultado_suma == 1000000000

        resultado_multiplicacion = calc.multiplicar(numero_grande, 2)
        assert resultado_multiplicacion == 1999999998

    def test_operaciones_con_decimales_precision(self, calc):
        """Test de precisión con números decimales"""
        a = 0.1
        b = 0.2
        resultado = calc.sumar(a, b)
        # Verificar que el resultado está cerca del esperado (problemas de flotantes)
        assert abs(resultado - 0.3) < 0.0001

    def test_operaciones_con_listas_vacias_y_valores_limite(self, calc):
        """Test con valores límite y casos edge"""
        # Listas con un solo elemento
        assert calc.promedio([42]) == 42
        assert calc.maximo([1]) == 1
        assert calc.minimo([1]) == 1

        # Operaciones con cero
        assert calc.multiplicar(0, 999) == 0
        assert calc.potencia(0, 5) == 0
        assert calc.valor_absoluto(0) == 0


@pytest.mark.integration
class TestIntegracionCompleta:
    """Pruebas de integración completas del sistema"""

    def test_simulacion_uso_real_calculadora(self, calc):
        """Simulación de uso real de la calculadora"""
        # Escenario: Calcular área de un círculo y estadísticas
        radio = 5
        pi_aproximado = 3.14159

        # Área = π * r²
        radio_al_cuadrado = calc.potencia(radio, 2)
        area = calc.multiplicar(pi_aproximado, radio_al_cuadrado)

        assert abs(area - 78.53975) < 0.001

        # Calcular estadísticas de varios círculos
        radios = [1, 2, 3, 4, 5]
        areas = []

        for r in radios:
            r_cuadrado = calc.potencia(r, 2)
            area_circulo = calc.multiplicar(pi_aproximado, r_cuadrado)
            areas.append(area_circulo)

        # Estadísticas de las áreas
        area_promedio = calc.promedio(areas)
        area_maxima = calc.maximo(areas)
        area_minima = calc.minimo(areas)

        assert area_maxima > area_promedio > area_minima
        assert area_minima == calc.multiplicar(pi_aproximado, 1)  # π * 1²

    def test_calculo_financiero_integracion(self, calc):
        """Test de integración para cálculos financieros básicos"""
        # Escenario: Calcular interés compuesto simple
        capital_inicial = 1000
        tasa_interes = 0.05  # 5%
        periodos = 3

        # Fórmula: M = C * (1 + i)^n
        uno_mas_interes = calc.sumar(1, tasa_interes)
        factor_multiplicador = calc.potencia(uno_mas_interes, periodos)
        monto_final = calc.multiplicar(capital_inicial, factor_multiplicador)

        # El resultado debería ser aproximadamente 1157.625
        assert abs(monto_final - 1157.625) < 0.001

        # Calcular ganancia
        ganancia = calc.restar(monto_final, capital_inicial)
        assert ganancia > 0
        assert abs(ganancia - 157.625) < 0.001


if __name__ == "__main__":
    pytest.main([__file__, "-v"])