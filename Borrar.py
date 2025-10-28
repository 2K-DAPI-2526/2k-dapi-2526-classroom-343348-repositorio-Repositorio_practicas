#Este programa permite el borrado de una linea concreta de cualquier archivo de texto.
import os
def borrar_linea_archivo(ruta_archivo, numero_linea):
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        
        if numero_linea < 1 or numero_linea > len(lineas):
            print("El número de línea está fuera de rango.")
            return
        
        del lineas[numero_linea - 1]
        
        with open(ruta_archivo, 'w') as archivo:
            archivo.writelines(lineas)
        
        print(f"Línea {numero_linea} eliminada correctamente.")
    
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
if __name__ == "__main__":
    ruta = input("Ingrese la ruta del archivo de texto: ")
    try:
        linea = int(input("Ingrese el número de línea a borrar: "))
        borrar_linea_archivo(ruta, linea)
    except ValueError:
        print("Por favor, ingrese un número válido para la línea.")

