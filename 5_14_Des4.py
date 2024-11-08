import math

# Excepción personalizada Se crea una clase y se define
class NegativeNumberError(Exception):
    def __init__(self, message="No se puede calcular la raíz cuadrada de un número negativo."):
        self.message = message
        super().__init__(self.message)

def calcular_raiz_cuadrada():
    try:
        # Solicitar el número al usuario
        numero = float(input("Ingresa un número para calcular su raíz cuadrada: "))
        
        # Verificar si el número es negativo
        if numero < 0:
            raise NegativeNumberError()  # Disparar la excepción personalizada si el número es negativo
        
        # Calcular la raíz cuadrada
        raiz = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {raiz}")

    except NegativeNumberError as e:
        print(f"Error: {e}")

    except ValueError:
        print("Error: Por favor ingresa un número válido.")

# Llamar a la función
calcular_raiz_cuadrada()
