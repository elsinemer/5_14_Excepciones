def leer_archivo(nombre_archivo):
    try:
        # Intentar abrir el archivo en modo lectura
        archivo = open(nombre_archivo, "r")
        contenido = archivo.read()
        print("Contenido del archivo:\n")
        print(contenido)
        
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
    
    finally:
        # Cerrar el archivo si fue abierto
        try:
            archivo.close()
            print("El archivo ha sido cerrado.")
        except NameError:
            print("El archivo no se abrió, por lo que no se necesita cerrarlo.")

# Solicitar el nombre del archivo al usuario
nombre_archivo = input("Ingresa el nombre del archivo que deseas abrir: ")
leer_archivo(nombre_archivo)
