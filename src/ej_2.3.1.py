# Ejercicio 2.3.1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

#Extra1: Lanzar excepciones conmensajes específicos si le edad es negativa, igual a 0 o superior a 125





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
                raise ValueError("La edad debe ser pmenor a 125")
            edad_incorrecta = True
        except ValueError as e:
            if edad is None:
                print(f"ERROR. El número introducido no es un entero válido")
            else:
                print(f"ERROR {e}. Intentalo de nuevo ")

    return edad

    
def mostrar_años_cumplidos(edad: int):
    for i in range(1, edad + 1):
        if i == edad:
            print(i)  
        else:
            print(i, end=",")




def main():
    edad = pedir_edad()
    print(f"Has cumplido los siguientes años: ")
    mostrar_años_cumplidos(edad)


if __name__ == "__main__":
    main()