try:
    num1 = int(input("Ingresa el primer número entero: "))
    num2 = int(input("Ingresa el segundo número entero: "))
    
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

except ValueError:
    print("Error: Por favor ingresa solo números enteros.")

else:
    # Se ejecuta si no hubo ninguna excepción
    print("La división se realizó correctamente.")
