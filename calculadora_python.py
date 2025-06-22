"""
Calculadora básica para demostrar integración continua
"""

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