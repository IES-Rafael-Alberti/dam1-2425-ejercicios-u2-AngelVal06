# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def comprobar_numero():
    num = int(input("Introduce un número entero: "))
    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")


def main():
    num_entero = comprobar_numero()


if __name__ == "__main__":
    main()