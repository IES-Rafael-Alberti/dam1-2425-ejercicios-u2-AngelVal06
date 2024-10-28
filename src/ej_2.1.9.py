# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.



def pedir_edad():
    try:
        edad = int(input("Dime tu edad: "))
    except ValueError:
        raise ValueError("Debes introducir un valor correcto.")
    return edad


def calcular_cantidad_dinero(edad):
    if edad < 4:
        print("La entrada es gratis")
    elif 4 <= edad < 18:
        print("La entrada cuesta 5€")
    elif edad > 18:
        print("La entrada cuesta 10€")


def main():
    try:
        edad = pedir_edad()
        calcular_cantidad_dinero(edad)
    except ValueError as e:
        print(f" {e}")


if __name__ == "__main__":
    main()