# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	            Puntuación
# Inaceptable	        0.0
# Aceptable	            0.4
# Meritorio	            0.6 o más

# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.


def  pedir_puntuacion():
    try:
        puntuacion = float(input("Dime la puntuación de rendimiento de tu empleado: "))
    except ValueError:
        raise ValueError("Debes introducir un número válido.")
    return puntuacion


def comprobar_nivel_rendimiento(puntos_rendimiento):
    if puntos_rendimiento == 0.0:
        print("El nivel de rendimiento de tu empleado es Inaceptable.")
    elif puntos_rendimiento == 0.4:
        print("El nivel de rendimiento de tu empleado es Aceptable.")
    elif puntos_rendimiento >= 0.6:
        print("El nivel de rendimiento de tu empleado es Meritorio.")


def calcular_cantidad_dinero(puntos_rendimiento):
    if puntos_rendimiento == 0.0:
        print(f"La cantidad de dinero es {(2400 * 0.0)+2400}")
    elif puntos_rendimiento == 0.4:
        print(f"La cantidad de dinero es {(2400 * 0.4)+2400}")
    elif puntos_rendimiento >= 0.6:
        print(f"La cantidad de dinero es {(puntos_rendimiento * 2400)+2400}")


def main():
    try:
        puntos_rendimiento = pedir_puntuacion()
        comprobar_nivel_rendimiento(puntos_rendimiento)
        calcular_cantidad_dinero(puntos_rendimiento)
    except ValueError as e:
        print(f" {e}")


if __name__ == "__main__":
    main()