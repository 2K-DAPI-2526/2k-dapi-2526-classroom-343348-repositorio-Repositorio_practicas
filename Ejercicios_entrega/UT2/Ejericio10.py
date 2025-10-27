#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
#Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
tipo_pizza = input("¿Quieres una pizza vegetariana? (s/n): ").lower()
if tipo_pizza == 's':
    print("Ingredientes vegetarianos disponibles: ")
    print("1. Pimiento")
    print("2. Tofu")
    eleccion = input("Elige un ingrediente (1/2): ")
    if eleccion == '1':
        ingrediente = "Pimiento"
    elif eleccion == '2':
        ingrediente = "Tofu"
    else:
        ingrediente = "Ingrediente no válido"
    es_vegetariana = True
elif tipo_pizza == 'n':
    print("Ingredientes no vegetarianos disponibles: ")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    eleccion = input("Elige un ingrediente (1/2/3): ")
    if eleccion == '1':
        ingrediente = "Peperoni"
    elif eleccion == '2':
        ingrediente = "Jamón"
    elif eleccion == '3':
        ingrediente = "Salmón"
    else:
        ingrediente = "Ingrediente no válido"
    es_vegetariana = False
else:
    ingrediente = "Tipo de pizza no válido"
    es_vegetariana = None
if es_vegetariana is True:
    print(f"Has elegido una pizza vegetariana con {ingrediente}, mozzarella y tomate.")
elif es_vegetariana is False:
    print(f"Has elegido una pizza no vegetariana con {ingrediente}, mozzarella y tomate.")
else:
    print("No se pudo determinar el tipo de pizza.")

