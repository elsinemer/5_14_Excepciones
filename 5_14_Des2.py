def operaciones_matematicas(lista):
    try:
        # Verificar que todos los elementos de la lista sean numéricos
        lista = [float(i) for i in lista]  # Convierte los elementos a flotantes, captura error de tipo si ocurre

        suma = sum(lista)
        producto = 1
        for num in lista:
            producto *= num

        # Cálculo del promedio
        promedio = suma / len(lista)

        print(f"Suma de los valores: {suma}")
        print(f"Producto de los valores: {producto}")
        print(f"Promedio de los valores: {promedio}")

    except ZeroDivisionError:
        print("Error: No se puede calcular el promedio de una lista vacía.")
    
    except TypeError:
        print("Error: La lista contiene elementos que no son numéricos.")
    
    except ValueError:
        print("Error: Por favor, asegúrate de que todos los elementos sean valores numéricos.")

# Ejemplo de uso:
lista_valores = input("Ingresa una lista de valores separados por comas: ").split(",")
operaciones_matematicas(lista_valores)
