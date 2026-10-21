"""
Caso. Se conoce el primer término A, la diferencia D y la cantidad N de términos de una  progresión. A y D son enteros entre -100 y 100, y N está entre 0 y 1000. Determine la suma de  los N términos; si N es cero, el total es cero. 

"""
A = int(input("Ingrese el primer término A: "))
D = int(input("Ingrese la diferencia D: "))
N = int(input("Ingrese la cantidad de términos N: "))

total = 0
termino = A
for i in range(N):
	total += termino
	termino += D

print(total)