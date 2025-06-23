"""
Calculadora básica para demostrar integración continua.
"""
import math
class Calculadora:
    """Clase que implementa operaciones matemáticas básicas"""
    
    def sumar(self, a, b):
        """Suma dos números"""
        return a + b
    
    def restar(self, a, b):
        """Resta dos números"""
        return a - b
    
    def multiplicar(self, a, b):
        """Multiplica dos números"""
        return a * b
    
    def dividir(self, a, b):
        """Divide dos números"""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    
    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        return base ** exponente
    
    def factorial(self, n):
        """Calcula el factorial de un número"""
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        if n == 0 or n == 1:
            return 1
        
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
    def modulo(self, a, b):
        """Devuelve el módulo de a % b"""
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a % b

    def promedio(self, numeros):
        """Calcula el promedio de una lista de números"""
        if not numeros:
            raise ValueError("La lista no puede estar vacía")
        return sum(numeros) / len(numeros)

    def es_par(self, n):
        """Devuelve True si el número es par, False si es impar"""
        return n % 2 == 0

    def raiz_cuadrada(self, x):
        """Devuelve la raíz cuadrada de x"""
        if x < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return math.sqrt(x)

    def valor_absoluto(self, x):
        """Devuelve el valor absoluto de x"""
        return abs(x)

    def redondear(self, numero, decimales):
        """Redondea un número a una cantidad específica de decimales"""
        try:
            return round(float(numero), int(decimales))
        except (ValueError, TypeError):
            raise ValueError("Los parámetros deben ser numéricos")
    
    def maximo(self, lista):
        """Devuelve el valor máximo de una lista"""
        if not lista:
            raise ValueError("La lista no puede estar vacía")
        return max(lista)

    def minimo(self, lista):
        """Devuelve el valor mínimo de una lista"""
        if not lista:
             raise ValueError("La lista no puede estar vacía")
        return min(lista)

    def logaritmo(self, x):
         """Devuelve el logaritmo en base 10 de un número positivo"""
         if x <= 0:
            raise ValueError("El logaritmo solo está definido para números positivos")
         return math.log10(x)

    def seno(self, x):
       """Devuelve el seno del ángulo x en radianes"""
       return math.sin(x)
    
def main():
    """Función principal para demostrar el uso de la calculadora"""
    calc = Calculadora()
    
    print("=== Calculadora Básica ===")
    print(f"5 + 3 = {calc.sumar(5, 3)}")
    print(f"10 - 4 = {calc.restar(10, 4)}")
    print(f"6 * 7 = {calc.multiplicar(6, 7)}")
    print(f"15 / 3 = {calc.dividir(15, 3)}")
    print(f"2^8 = {calc.potencia(2, 8)}")
    print(f"5! = {calc.factorial(5)}")

if __name__ == "__main__":
    main()