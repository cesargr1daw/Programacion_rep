"""
6. Haz un programa que permita calcular la suma de dos números. Pedirá dos
números al usuario y mostrará su suma, volviendo a repetir hasta que ambos
números introducidos sean 0."""
num1=float(input("Introduce el primer número: "))
num2=float(input("Introduce el segundo número: "))
while not (num1==0 and num2==0):
    print(num1+num2)
    num1=float(input("Vuelve a introducir el primer número: "))
    num2=float(input("Vuelve a introducir el segundo número: "))