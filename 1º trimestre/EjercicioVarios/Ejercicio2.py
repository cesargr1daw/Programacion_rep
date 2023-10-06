"""
2. Diseña un programa que lee un número y calcula el número elevado a 2. El
programa deja de calcular cuadrados cuando el usuario introduce un número
negativo.
"""
num=int(input("Introduce una raíz: "))
print(f"El número {num} elevado a 2 es: {num**2}")
while num>0:
    num=int(input("Introduce otra raíz: "))
    print(f"El número {num} elevado a 2 es: {num**2}")
