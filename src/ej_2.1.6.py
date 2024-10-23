# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


def pedir_sexo():
    return input("Dime cual es tu sexo: ").lower()


def pedir_nombre():
    return input("Dime cual es tu nombre: ").upper()


def main():
    sexo = pedir_sexo()
    nombre = pedir_nombre()
    if sexo == "mujer" and nombre[0] < "M":
        print("Eres del grupo A.")
    elif sexo == "hombre" and nombre[0] > "N":
        print("Eres del grupo A.")
    else:
        print("Eres del grupo B.")


if __name__ == "__main__":
    main()
