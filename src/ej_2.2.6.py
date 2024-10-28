# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

import os
def borrar_pantalla():
    os.system("cls")


def pedir_numero():
    try:
        numero = int(input("Dime un número entero: "))
        if numero < 0:
            raise ValueError("El número no puede ser negativo!")
    except ValueError:
        raise ValueError("Debe ser un número entero y positivo!")
    return numero


def hacer_triangulo(numero):
    for i in range(1, numero + 1):
        print("*"*i)


def main():
    borrar_pantalla()
    try:
        numero = pedir_numero()
        hacer_triangulo(numero)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()