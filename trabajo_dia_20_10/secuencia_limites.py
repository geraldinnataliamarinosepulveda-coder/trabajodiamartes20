"""
Caso. Una pantalla debe presentar todos los enteros comprendidos entre dos límites A y B,  ambos incluidos, empezando por A y terminando en B. Los límites son enteros entre -100 y  100. Si coinciden, presente ese único valor. 

"""
A = int(input("Ingrese el limite A: "))
B = int(input("Ingrese el limite B: "))

for i in range(A, B + 1):
    print(i)