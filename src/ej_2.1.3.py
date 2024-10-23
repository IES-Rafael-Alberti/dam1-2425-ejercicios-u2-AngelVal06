# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


def comprobar_division():
    dividendo = int(input("Dime el dividendo: "))
    divisor = int(input("Dime el divisor: "))
    if dividendo == 0 or divisor == 0:
        print("**ERROR** Ningún número puede ser cero.")
    else:
        resultado = dividendo / divisor
    print(resultado)
    


def main():
    division = comprobar_division()


if __name__ == "__main__":
    main()


