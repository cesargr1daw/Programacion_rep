"""
3. Programa que te pide un número y:
○ Va recorriendo los números desde el introducido hasta el 7,
imprimiendolos.
○ Además calcula la suma de estos números.
"""
num=int(input("Introduce un número: "))
suma=0
if num<7:
    for i in range(num,7,+1):
        suma+=i
        print(i)
elif num>7:
    for i in range(7,num):
        suma+=i
        print(i)
print("La suma es total es",suma)