# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.




def preguntar_palabra():
    palabra = input("Dime una palabra. ")
    return palabra


def bucle(palabra):
    for i in range(10):
        print(palabra)



def main():
    palabra = preguntar_palabra()
    bucle(palabra)



if __name__ == "__main__":
    main()
