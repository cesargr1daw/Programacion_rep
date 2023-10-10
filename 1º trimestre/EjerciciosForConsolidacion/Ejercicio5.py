numero = int(input("Introduce un número: "))
while numero > 0:
    digito = numero % 10 # obtiene el último dígito del número
    print(digito) #lo imprime por pantalla
    numero //= 10 #para eliminar el dígito obtenido anteriormente
