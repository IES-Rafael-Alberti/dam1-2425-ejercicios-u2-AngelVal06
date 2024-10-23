# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.


def validar_edad(edad: int):
    if edad < 16:
        raise Exception("No puede tributar.")


def validar_ingresos(ingresos: float):
    if ingresos < 1000:
        raise Exception("No puede tributar.")


def pedir_entero(mensaje: str)-> int:
    try:
        edad = int(input("Introduce tu edad: "))
    except ValueError:
        raise ValueError("Debe introducir un valor entero!")
    
    return edad

def pedir_importe(mensaje: str) -> float:
    try:
        ingresos_mensuales = float(input("Introduce tus ingresos mensuales: "))
    except ValueError:
        raise ValueError("Debe introducir un valor coherente!")
    
    return ingresos_mensuales

def comprobar_si_tributa():
    try:
        edad = pedir_entero("Introduce tu edad: ")

        ingresos_mensuales = pedir_importe("Introduce tus ingresos mensuales: ")

        validar_edad(edad)

        validar_ingresos(ingresos_mensuales)
        
        if edad > 16 and ingresos_mensuales >= 1000:
            print("Puede tributar.")

    except ValueError as e:
        print(f" {e}")
    except Exception as e:
        print(f"{e}")


def main():
    impuestos = comprobar_si_tributa()



if __name__ == "__main__":
    main()

