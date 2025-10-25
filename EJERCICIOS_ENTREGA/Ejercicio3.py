
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
if num2 == 0:
    print("Error: No se puede dividir por cero")
else:
    print("El resultado de la división es:", num1 / num2)
# --- IGNORE ---

