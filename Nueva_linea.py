#Permite añadir nueva linea en cualquier archivo de texto desde terminal e indique la fecha de modificación
import sys
from datetime import datetime
def anadir_linea_a_archivo_con_fecha(nombre_archivo, nueva_linea):
    try:
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        linea_con_fecha = f"{fecha_actual}: {nueva_linea}"
        with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(linea_con_fecha + '\n')
        print(f"Línea añadida al archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python AnadirRespuesta.py <nombre_archivo> <nueva_linea>")
    else:
        nombre_archivo = sys.argv[1]
        nueva_linea = sys.argv[2]
        anadir_linea_a_archivo_con_fecha(nombre_archivo, nueva_linea)   

#Programa que pide nombre de archivo de texto y añade una linea debajo de la última pidiendolo desde terminal
