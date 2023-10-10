"""
4. Modifica el programa anterior para que sólo pinte el borde del cuadrado
* * * *
*     *
*     *
* * * *
"""
numero = int(input("Introduce un número: "))
for i in range(numero):
    if i == 0 or i == numero - 1:
        print("* " * numero)
    else:
        print("* " + "  " * (numero - 2) + "*")
