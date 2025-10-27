
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.
num1 = float(input("Introduce el dividendo: "))
num2 = float(input("Introduce el divisor: "))
if num2 == 0:
    print("Error: No se puede dividir entre cero.")
else:
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")

