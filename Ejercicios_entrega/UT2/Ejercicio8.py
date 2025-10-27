#En una determinada empresa, sus empleados son evaluados al final de cada año. 
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. 
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, 
# pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
#Nivel              Puntuación
#Inaceptable        0.0
#Aceptable          0.4    
#Meritorio          0.6 o más
#Escribir un programa que pregunte al usuario su puntuación en la evaluación y muestre por pantalla la cantidad de dinero que recibirá el usuario.
puntuacion = float(input("Introduce tu puntuación en la evaluación (0.0, 0.4, 0.6 o más): "))
if puntuacion == 0.0:
    nivel = "Inaceptable"
    dinero = 0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = 2400 * puntuacion
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero = 2400 * puntuacion
else:
    nivel = "Puntuación inválida"
    dinero = 0
print(f"Nivel: {nivel}")
print(f"Cantidad de dinero que recibirás: {dinero}€")
