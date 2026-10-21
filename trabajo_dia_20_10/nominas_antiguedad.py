"""
Caso. Se reciben N empleados, con 1 ≤ N ≤ 40. Cada registro contiene, en este orden,  identificador entero positivo único, edad entera no negativa en años y años enteros de  antigüedad entre 1 y 50. El sueldo ficticio es la suma de una base de 100 unidades monetarias,  el valor numérico de la edad y la suma de los enteros desde 1 hasta la antigüedad; toda esa  suma se divide entre los años de antigüedad. La edad y la suma de años se consideran aportes  numéricos en unidades monetarias dentro de este modelo ficticio. Informe el sueldo de cada 
empleado, el total de la nómina y los identificadores con mayor y menor sueldo. En empate  conserve el primero recibido. 


"""
N = int(input("Ingrese la cantidad de empleados: "))

total = 0
mayor = None
menor = None
id_mayor = 0
id_menor = 0

for i in range(N):
    print("Empleado", i + 1)

    identificador = int(input("Ingrese el identificador: "))
    edad = int(input("Ingrese la edad: "))
    antiguedad = int(input("Ingrese los años de antiguedad: "))

    suma = antiguedad * (antiguedad + 1) / 2
    sueldo = (100 + edad + suma) / antiguedad

    print("Sueldo:", round(sueldo, 2))

    total += sueldo

    if mayor is None or sueldo > mayor:
        mayor = sueldo
        id_mayor = identificador

    if menor is None or sueldo < menor:
        menor = sueldo
        id_menor = identificador

print("Total de la nomina:", round(total, 2))
print("Identificador con mayor sueldo:", id_mayor)
print("Identificador con menor sueldo:", id_menor)