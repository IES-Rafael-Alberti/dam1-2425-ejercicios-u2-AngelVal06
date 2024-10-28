# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

import os

def borrar_pantalla():
    os.system("cls")



def preguntar_pizza():
    pizza = input("¿Quieres una pizza vegetariana? ")
    if pizza == "si":
        pizza_vegetariana()
    elif pizza == "no":
        pizza_no_vegetariana()
    else:
        print("Debes elegir una si quieres una pizza vegetariana o no.")


def pizza_vegetariana():
    print("El menú de la pizza vegetariana lleva mozzarella y tomate puedes elegir uno de estos ingredientes aparte: Pimiento y tofu.")
    ingrediente = input("Elige uno de los ingredientes. ")
    print(f"Tu menú de pizza vegetariana lleva mozzarella, tomate y {ingrediente}")
    


def pizza_no_vegetariana():
    print("El menú de la pizza no vegetariana lleva mozzarella y tomate puedes elegir uno de estos ingredientes aparte: Peperoni, jamón y salmón.")
    ingrediente = input("Elige uno de los ingredientes. ")
    print(f"Tu menú de pizza no vegetariana lleva mozzarella, tomate y {ingrediente}")
    


def main():
    borrar_pantalla()
    preguntar_pizza()



if __name__ == "__main__":
    main()