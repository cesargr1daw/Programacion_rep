"""
4. Modifica el programa anterior para que sólo pinte el borde del cuadrado
* * * *
*     *
*     *
* * * *
"""
printar=int(input("Introduce el número que va a printar: "))
for i in range(printar):
    if i == 0 or i == printar - 1:
        print("* " * printar)
    else:
        print("* " + "  " * (printar - 2) + "*")
