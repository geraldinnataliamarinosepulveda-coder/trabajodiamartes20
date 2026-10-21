"""

Fórmula o relación: Nómina = sueldo₁ + sueldo₂ + … + sueldoₙ. 



"""

empleados = int(input())
total_nomina = 0.0

for i in range(empleados):
    total_nomina += float(input())

print(total_nomina)