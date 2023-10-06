"""
9. Pedir un número y calcular su factorial.
Ejemplo:
Factorial de 5:
5! = 5x4x3x2x1 = 120
"""
n=int(input("Introduce el numero del que quieres el factorial: "))
factorial=1
for i in range (n,1,-1):
    factorial*=i
print(factorial)