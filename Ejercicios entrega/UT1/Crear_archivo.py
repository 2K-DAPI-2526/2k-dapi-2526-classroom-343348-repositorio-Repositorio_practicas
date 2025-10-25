#Para crear nuestro primer archivo, tendremos que darle al botón de añadir nuevo archivo a nuestra carpeta
#Escribiremos el nombre, y después le tendremos que poner la extensión .txt o .py, en función del tipo de archivo que queramos.
#El .txt, abrirá un archivo de texto nuevo dentro de nuestra carpeta, y el .py creará
#un archivo python dentro de nuestra carpeta que podremos abrir con VS code
#Vamos a ello:

#Abrir la carpeta creada desde VSCodev de la siguiente forma:
open ("miarchivo.txt","w")

#El programa generará un archivo con el nombre miarchivo de tipo txt
#En el caso que queramos abrir un archivo .py, lo haremos de la siguiente forma

open ("miarchivo.py","w")

#Dale a Run y mira si los dos archivos se han creado en viestra carpeta.
#Debería haber en tu carpeta únicamente dos archivos, los dos creados anteriormente, uno .txt y otro .py con el nombre que les hayas dado.
#Si es así, felicidades, acabas de generar tus dos primeros archivos usando VSCode.

#Vamos a ir ahora más allá, vamos a intentar generar un prorgama en el archivo .py que permita añadir información de tipo texto dentro del archivo .txt

#Para ello,abriremos el archivo .py haremos lo siguiente:

f = open("miarchivo.txt","w") # para abrir el archivo
f.write ("Este es mi archivo") # Para escribir en el 


#Con esto, ya abremos grabado en nuestro archivo .txt nuestra primera frase.

#Vamos a hacer una prueba de que todo funciona correctamente, vamos a guardar información tuya en el archivo y vas a comprobar que efectivamente se a guardado correctamente.
#Borramos el contenido (Si lo deseamos)
with open("miarchivo.txt", "w", encoding="utf-8") as f:
    f.write("Este es el nuevo contenido.\n")
    f.write("El contenido anterior se ha borrado.")
#Por ejemplo, vamos a guardar tus datos por consola y vamos a utilizar la terminal para introducir los datos manualmente que nos pida el programa.


print ("Introduce ut Nombre y apellidos")
Nombre = str (input("Nombre: "))
Apellidos = str (input("Apellidos: "))


#Si le das a Run, verás que el programa te pide estos datos y los guarda
#Para añadirlos al fichero .txt, tendremos que hacer lo siguiente:

#Primero, abrimos el archivo .txt en modo escritura

with open("miarchivo.txt", "w", encoding="utf-8") as f:
    f.write(Nombre)
    f.write(Apellidos)

#Prueba ahora y dale a Run, no olvides que tienes que estar en tu carpeta para que los archivos se guarden, si no, estos dos arhcivos aparecerán en otra ruta
#Por eso es importante fijarte bien en la dirección que devuelve la terminal, si tu carpeta la has creado como MiarchivoPython, asegurate
#de que en la terminal figura lo siguiente C:\Users\hp\Desktop\MiarchivoPython
#Si no figura esa ruta, quiere decir que no estamos creando los arhcivos donde debemos y puede suponer un problema
#Si has conseguido crear esos dos archivos dentro de tu carpeta y añadir información al .txt con el .py, Enhorabuena! podemos pasar al siguiente nivel.
#Esto quiere decir que hemos escrito sobre lo que anteriormente habíamos grabado.
#Para borrar lo anteriormente guardado debemos hacerlo de la siguiente manera:

# with open("miarchivo.txt", "w", encoding="utf-8") as f:
  #  f.write("Este es el nuevo contenido.\n")
   # f.write("El contenido anterior se ha borrado.")

# Este códgi, ponlo ahí donde desees que se borre el contenido de tu archivo.

import os

# Definir carpeta y archivo
carpeta = "MiarchivoPython"
archivo = "mi_archivo.txt"

# Crear carpeta si no existe
os.makedirs(carpeta, exist_ok=True)

# Ruta completa del archivo
ruta = os.path.join(carpeta, archivo)

#Pedir nombre y apellidos
Nombre=input("Introduce tu nombre: ")
Apellido=input("Introduce tu apellido:")

# Crear y escribir en el archivo
with open(ruta, "w") as f:
    f.write(Nombre)
    f.write(Apellido)