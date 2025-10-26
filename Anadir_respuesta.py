#Este programa servirá para añadir respuestas a las dudas generales que vayan surgiendo en el módulo de DAPI en el arhcivo Dudas.txt
import datetime
ruta_dudas = "C:/Users/hp/Desktop/Javi-REPO-DAPI/REPOSITORIO_PRACTICAS_2K/Dudas"
with open(ruta_dudas, "a", encoding="utf-8") as archivo_dudas:
    respuesta = input("Ingrese la respuesta a la duda: ")
    fecha_hora_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    archivo_dudas.write(f"{fecha_hora_actual}: {respuesta}\n")
print("Respuesta añadida correctamente al archivo Dudas.txt")
