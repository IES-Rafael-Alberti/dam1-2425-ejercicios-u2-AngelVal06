# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
import os
def borrar_pantalla():
    os.system("cls")

    
def preguntar_número():
    numero = int(input("Dime un número entero positivo: "))
    if numero < 0:
        print("El número no puede ser negativo.")
    return numero


def comprobar_número(numero):
    cadena = ""
    for i in range (1, numero + 2, 2):   
        if i == numero:
            cadena += f"{i}"
        else:
            cadena += f"{i}, "
    print(cadena)


def main():
    borrar_pantalla()
    numero = preguntar_número()
    comprobar_número(numero)


if __name__ == "__main__":
    main()