def calcular_factorial():
    try:
        # Solicitar el número al usuario
        numero = int(input("Ingresa un número entero positivo: "))
        
        # Verificar si el número es negativo
        if numero < 0:
            raise ValueError("El número debe ser un entero positivo.")
        
        # Calcular el factorial
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i

        print(f"El factorial de {numero} es: {factorial}")

    except ValueError as e:
        print(f"Error: {e}")

    except OverflowError:
        print("Error: El número es demasiado grande para calcular su factorial.")

    except Exception as e:
        print(f"Error inesperado: {e}")

# Llamar a la función
calcular_factorial()
