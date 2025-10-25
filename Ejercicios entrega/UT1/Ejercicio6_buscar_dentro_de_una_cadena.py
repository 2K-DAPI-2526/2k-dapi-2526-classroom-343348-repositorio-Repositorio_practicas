#Implementa un programa que buscque un valor alfanumérico dentro de una cadena de caracteres introducida por el usuario.
#El programa contará cuantas veces se repite ese caracter dentro de la cadena y devolverá el número de veces que se repite
#El programa devolverá lo siguiente: "En la frase que has introducido, la letra "o" se repite x veces", por ejemplo
#El carácter a buscar es a tu criterio (escoge una vocal o consonante para que sea más fácil buscar)



# Programa que cuenta el número de "o" en una cadena

# Pedir al usuario una cadena
texto = input("Escribe una cadena de caracteres: ")

# Contar las 'o' (minúsculas)
contador = texto.count("o")

# También puedes contar mayúsculas si quieres
contador_total = texto.lower().count("o")

print(f"Número de 'o' minúsculas: {contador}")
print(f"Número total de 'o' (mayúsculas y minúsculas): {contador_total}")

