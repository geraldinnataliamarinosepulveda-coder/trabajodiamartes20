"""
Caso. Se reciben los tiempos de N ciclistas, con 1 ≤ N ≤ 20, sobre una vuelta de 250 metros.  Cada registro contiene identificador entero positivo único, minutos enteros no negativos,  segundos entre 0 y 59 y centésimas entre 0 y 99. Cada tiempo total es positivo. Informe la  velocidad media de cada ciclista en kilómetros por hora y el identificador del ganador. En  empate de tiempo gana el primero recibido. 

"""
N = int(input("Ingrese la cantidad de ciclistas: "))

menor = None
ganador = 0

for i in range(N):
    print("Ciclista", i + 1)

    identificador = int(input("Ingrese el identificador: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    centesimas = int(input("Ingrese las centesimas: "))

    T = minutos * 60 + segundos + centesimas / 100
    velocidad = 0.25 / (T / 3600)

    print("Velocidad media:", round(velocidad, 2), "km/h")

    if menor is None or T < menor:
        menor = T
        ganador = identificador

print("El identificador del ganador es:", ganador)