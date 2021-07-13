
from datetime import datetime
import matplotlib.pyplot as plt

def chart_bar(tiempo, ganancias):
    fig, ax = plt.subplots()
    rects1 = ax.bar(tiempo, ganancias, color="green")
    ax.set_title('Tiempo X Ganancias del 2018 - 2021')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Ganancias')
    ax.bar_label(rects1, padding=3)
    #plt.savefig('chart_bar_green.svg')
    plt.show()

while True:
    n = int(input("TIEMPO TRANSCURRIDO \n"
                  "1. SEMANAL \n"
                  "2. SALIR \n"
                  "Elija una opcion: "))
    if n == 1:
        a = int(input("Ingreso del lunes: "))
        b = int(input("Ingreso del martes: "))
        c = int(input("Ingreso del miercoles: "))
        d = int(input("Ingreso del jueves: "))
        e = int(input("Ingreso del viernes: "))
        f = int(input("Ingreso del sabado: "))
        g = int(input("Ingreso del domingo: "))
        tiempo = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        ganancia = [a, b, c, d, e, f, g]
        chart_bar(tiempo, ganancia)
        total = a + b + c + d + e + f + g
        now = datetime.now()
        horas_actual = now.strftime("%H:%M:%S")
        print("El Ingreso de la SEMANA es:", total)
        print("HORA ACTUAL: ", horas_actual)
    else:
        break