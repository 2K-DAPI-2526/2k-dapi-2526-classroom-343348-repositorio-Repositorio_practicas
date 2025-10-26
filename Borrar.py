    #Este programa borra el contenido de cualquier archivo de texto introduciendolo por terminal
import sys
def borrar_contenido_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write('')
        print(f"Contenido del archivo '{nombre_archivo}' borrado.")
    except Exception as e:
        print(f"Error al borrar el contenido del archivo: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python Borrar.py <nombre_archivo>")
    else:
        nombre_archivo = sys.argv[1]
        borrar_contenido_archivo(nombre_archivo)
