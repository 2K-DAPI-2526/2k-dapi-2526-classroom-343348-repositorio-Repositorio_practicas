#Programa que añadirá nueva línea al archivo de texto Noticias.txt
with open("Noticias.txt", "a") as archivo:
    nueva_noticia = input("Ingrese la nueva noticia: ")
    archivo.write(nueva_noticia + "\n")
# Abre el archivo en modo de añadir ('a')
# Solicita al usuario que ingrese una nueva noticia
# Escribe la nueva noticia en el archivo seguida de un salto de línea
# Cierra el archivo automáticamente al salir del bloque 'with'

