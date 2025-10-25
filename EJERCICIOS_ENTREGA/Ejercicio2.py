#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla 
# si la contraseña introducida por el usuario coincide con la guardada 
# en la variable sin tener en cuenta mayúsculas y minúsculas.


Contraseña = "Contraseña"
Contraseña_usuario = input("Introduce la contraseña: ")
if Contraseña_usuario.lower() == Contraseña.lower():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
    
