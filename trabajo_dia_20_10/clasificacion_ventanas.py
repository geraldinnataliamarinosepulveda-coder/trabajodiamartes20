"""
Caso. Un vendedor tiene N ventas, con 0 ≤ N ≤ 1000, y se recibe el importe no negativo de cada  una. Informe cuántas fueron de 200 o menos, cuántas superaron 200 sin llegar a 400 y cuántas  fueron de 400 o más. Una venta pertenece a un solo grupo. 

"""
N = int(input("Ingrese la cantidad de ventas: "))

grupo1 = 0
grupo2 = 0
grupo3 = 0

for i in range(N):
    importe = float(input("Ingrese el importe de la venta: "))

    if importe <= 200:
        grupo1 += 1
    elif importe < 400:
        grupo2 += 1
    else:
        grupo3 += 1

print("Ventas de 200 o menos:", grupo1)
print("Ventas mayores de 200 y menores de 400:", grupo2)
print("Ventas de 400 o más:", grupo3)