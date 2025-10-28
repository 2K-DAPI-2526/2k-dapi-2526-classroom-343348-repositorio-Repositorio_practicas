#Programa que leer cualquier archivo de texto y muestra su contenido en pantalla.
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo de texto a leer: ")
    leer_archivo(nombre_archivo)

# -*- coding: utf-8 -*-
