#Este archivo servirá para añadir un nuevo hilo de dudas en el archivo Dudas.txt
ruta_dudas = "Dudas.txt"
nueva_duda = input("Ingrese la nueva duda: ")
with open(ruta_dudas, "a", encoding="utf-8") as archivo:
    archivo.write(nueva_duda + "\n")
print("Duda añadida correctamente.")
