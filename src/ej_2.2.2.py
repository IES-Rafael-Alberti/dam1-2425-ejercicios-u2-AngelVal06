# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


def pregunta_edad():
    edad = int(input("Dime tu edad: "))

    for i in range(1, edad +1):
        print(i)





def main():
    pregunta_edad()


if __name__ == "__main__":
    main()


