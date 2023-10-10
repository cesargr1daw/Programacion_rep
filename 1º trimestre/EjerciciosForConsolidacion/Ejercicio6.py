numero = int(input("Introduce un número: "))
suma=0
while numero > 0:
    digito = numero % 10 # obtiene el último dígito del número
    suma+=digito #vamos sumando cada digito
    numero //= 10 #para eliminar el dígito obtenido anteriormente