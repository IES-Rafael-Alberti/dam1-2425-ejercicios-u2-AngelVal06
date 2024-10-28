# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
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
    for i in range (numero, -1, -1):   
        if i == 0:
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