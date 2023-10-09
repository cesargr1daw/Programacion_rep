"""
5. Construye un programa que calcule el resultado de un número elevado a otro
número. Ambos números deben recibirse por teclado. Deberás calcular el
resultado realizando multiplicaciones y no el operador ** (potencia)
Es decir, imagina que ponemos el 3 y 4. El programa deberá calcular 3⁴
"""
base=int(input("Introduce la base: "))
expt=int(input("Introduce el exponente: "))
resl=1
while expt>0:
    resl*=base
    expt=expt-1
print(resl)