"""
7. Crea un programa que seleccione un número aleatorio y el usuario debe
adivinarlo. El bucle while se ejecuta hasta que el usuario adivine
correctamente. Rango del 1 al 10.
"""
import random
alt_num = random.randint(1,10)
errores=0
adivina_num=int(input("Intenta acertar el número secreto: "))
while adivina_num!=alt_num:
    print("¡¡¡Fallaste!!!")
    if alt_num>adivina_num:
        print("El número es mayor al que has introducido")
    else:
        print("El número es menor al que has introducido")
    errores+=1
    adivina_num=int(input("Intenta acertar el número secreto de nuevo: "))
print(f"¡¡¡Felicidades!!! Has acertado, aunque has fallado {errores} veces")