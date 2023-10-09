"""
8. Escribe un programa que trabaje como una caja registradora. El usuario
introducirá precios de productos y el sistema irá sumando cada precio. El
sistema sabrá que debe imprimir el resultado de la suma cuando el usuario
introduzca un valor negativo.
"""
precio=float(input("Introduce el precio del producto: "))
valorTotal=0
while precio>=0:
    valorTotal+=precio
    precio=float(input("Introduce el precio de otro producto: "))
print(f"El precio total es: {valorTotal}€")