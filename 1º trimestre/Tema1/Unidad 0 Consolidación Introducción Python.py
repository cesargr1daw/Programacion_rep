"""Ejercicio 1: Crea un programa en python que escriba en pantalla el producto de
dos números prefijados."""
num1= 2
num2= 3
print(num1*num2)

"""Ejercicio 2: Crea un programa que muestre el resto de dividir dos números
prefijados."""
num1= 10
num2= 3
print(num1%num2)

"""Ejercicio 3: Crea un programa que calcule y muestre la media aritmética de
dos números enteros introducidos por el usuario. Hay que tener en cuenta
que la media aritmética puede contener decimales."""
num1= 10
num2= 3
print((num1+num2)/2)

"""Ejercicio 4: Crea un programa que pida al usuario una longitud en millas (por
ejemplo, 3) y calcule su equivalencia en metros (1 milla = 1609 m)."""
milla=int(input("Introduce el número de millas: "))
metro= milla*1609
print(f"{milla} millas son {metro}metros")

"""Ejercicio 5: Crea un programa que pida al usuario una temperatura en grados
centígrados y calcule (y muestre) a cuántos grados Fahrenheit equivalen (F =
9*C/5 + 32)."""
gradosC=int(input("Introduce el número de Cº: "))
gradosF= 9*gradosC/5 + 32
print(f"{gradosC}ºC son {gradosF}ºF")

"""Ejercicio 6: Realiza un programa que pida al usuario cuatro notas decimales y
muestre la parte entera de su media aritmética."""
nota1=float(input("Introduce la 1º nota: "))
nota2=float(input("Introduce la 2º nota: "))
nota3=float(input("Introduce la 3º nota: "))
nota4=float(input("Introduce la 4º nota: "))
media=(nota1+nota2+nota3+nota4)//4

print(f"La media de {nota1}+{nota2}+{nota3}+{nota4} es: {media}")

"""Ejercicio 7: Realiza un programa en python que pida al usuario la base y altura
de un triángulo y muestre su área."""
base=float(input("Introduce la base del triángulo: "))
altura=float(input("Introduce la altura del triángulo: "))
area=base*altura/2.0
print(f"El area total del triángulo es: {area}")

"""Ejercicio 8: Realizar un programa que lea una cantidad de horas, minutos y
segundos, y los transforme en una expresión de tiempo convencional en la
que los minutos y segundos estén dentro del rango [0,59]. Por ejemplo, dadas
10 horas, 119 minutos y 280 segundos, debería dar como resultado 12 horas,
3 minutos y 40 segundos"""
