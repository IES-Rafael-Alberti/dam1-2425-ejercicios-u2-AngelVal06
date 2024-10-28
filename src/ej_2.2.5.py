# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
#    amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
import os 
def borrar_pantalla():
    os.system("cls")


def calcular_capital_por_año(inversion, interes, años):
    inversion *= 1 + interes / 100
    for i in range(1, años):









def main():
    borrar_pantalla()
    inversion = float(input("Cantidad a invertir: "))
    interes = float(input("Cantidad de interés anual: "))
    años = int(input("Cantidad de años: "))
    calcular_capital_por_año(inversion, interes, años)




if __name__ == "__main__":
    main()