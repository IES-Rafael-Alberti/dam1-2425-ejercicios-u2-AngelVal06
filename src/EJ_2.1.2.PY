# Ejercicio 2.1.2¶
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.





def comprobar_contraseña(contraseña):
    contraseña_correcta = "contraseña"

    if contraseña == contraseña_correcta:
        print("Esa es la contraseña")
    else:
        print("**ERROR**")
    


def main():
    contraseña = input("¿Cual es la contraseña? ")

    comprobar_contraseña(contraseña.lower())


if __name__ == "__main__":
    main()