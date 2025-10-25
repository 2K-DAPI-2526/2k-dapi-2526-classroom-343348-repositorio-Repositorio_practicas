#Implimenta un programa que pide al usuario su numero de DNI con letra, y separe la parte numérica de la letra.
#Ten en cuenta que el número del Documento Nacional de Identificación consta de 8 dígitos y una letra.
#El programa devolverá por una parte el número del DNI y por otra la letra en MAYUSCULAS 


DNI = str(input("Introduce tu DNI: "))

Numero = int(DNI[0:8])
Letra = DNI[8]

print ("El Numero de tu DNI es: ",Numero)
print ("La letra de tu DNI es: ",Letra)