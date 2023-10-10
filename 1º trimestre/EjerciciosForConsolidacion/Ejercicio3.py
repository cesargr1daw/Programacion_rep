"""
Construye un programa que dado un número me pinte un cuadrado con
tantos * por fila como ese número. Por ejemplo, para número = 4
* * * *
* * * *
* * * *
* * * *
"""
printar=int(input("Introduce el número que va a printar: "))
for i in range(printar):
    print("*" * printar)
