"""
Caso. Una inversión ficticia inicia con capital C no negativo y mantiene una tasa anual  porcentual I con 0 < I < 100. Se recibe también un entero M entre 0 y 50. El interés de cada año es el saldo al comienzo de ese año multiplicado por I y dividido entre 100; se suma al saldo al  final del año. Determine el saldo después de M años; con M = 0 conserva el capital inicial. 

"""

capital=float(input("ingrese el capital inicial: "))
i= float (input("ingrese la tasa de interes anual : "))
M = float(input("ingrese el numero de años :"))
saldo = "c"


for aniI in range(M):
    interes = capital * i / 100
capital = capital + interes 

print("el saldo final es :", capital)