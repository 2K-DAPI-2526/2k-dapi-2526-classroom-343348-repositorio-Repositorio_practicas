#Lo primero es lo primero, vamos a crear tu carpeta en el escritorio
#Para ello, vamos a hacer de la siguiente manera:
#Los primero, inicializamos el programa con la siguiente secucencia:
import os
# Esto nos permite manipular el sistema operativo

# Después, se obtiene la ruta del escritorio según el sistema operativo, o donde queramos guardarlo
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Nombre de la carpeta que quieres crear
folder_name = "MiarchivoPython"

# Ruta completa de la carpeta
folder_path = os.path.join(desktop, folder_name)

# Crear la carpeta (si no existe)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Carpeta creada en: {folder_path}")
else:
    print("La carpeta ya existe.")

#Una vez tengamos la carpeta, ya podremos comenzar a guardar los archivos de programa
#Para crear un archivo, tendremos que abrir la carpeta dándole a Open Folder, y seleccionando la carpeta creada
