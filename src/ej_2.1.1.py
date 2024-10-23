# EJERCICIO: 2.1.1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.


def pedir_edad() -> int:
    edad_incorrecta = False
    while not edad_incorrecta:
        try:
            edad = None
            edad = int(input("Introduce tu edad: "))
            if edad < 0:
                raise ValueError("La edad debe ser positivo")
            if edad == 0:
                raise ValueError("La edad debe ser positivo mayor que cero")
            if edad > 125:
                raise ValueError("La edad debe ser menor a 125")
            edad_incorrecta = True
        except ValueError as e:
            if edad is None:
                print(f"ERROR. El número introducido no es un entero válido")
            else:
                print(f"ERROR {e}. Intentalo de nuevo ")

    return edad


def comprobar_años(edad):
    if edad < 18:
        print("No eres mayor de edad.")
    else:
        print("Eres mayor de eada.")



def main():
    edad = pedir_edad()
    comprobar_años(edad)
    

if __name__ == "__main__":
    main()