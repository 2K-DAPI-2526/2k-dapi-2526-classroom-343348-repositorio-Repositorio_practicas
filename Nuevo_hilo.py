#Programa que permite añadir nuevo hilo de un foro o duda general al archivo Dudas.txt
import datetime
def anadir_duda(duda):
    with open("Dudas.txt", "a", encoding="utf-8") as archivo:
        fecha_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        archivo.write(f"{fecha_hora}: {duda}\n")
if __name__ == "__main__":
    nueva_duda = input("Ingrese su duda general: ")
    anadir_duda(nueva_duda)
    print("Duda añadida correctamente.")

