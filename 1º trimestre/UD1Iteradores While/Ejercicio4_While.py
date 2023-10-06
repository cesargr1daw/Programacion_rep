"""
4. Construye un programa que pida al usuario que ingrese números hasta que
ingrese un cero y luego muestra la suma de los números ingresados."""
num=int(input("Introduce un número entero: "))
suma=0
while num!=0:
    suma+=num
    num=int(input("Vuelve a introducir un número entero: "))
print(suma)