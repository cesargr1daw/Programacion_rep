"""
9. Modifica tu programa para que también lleve la cuenta del impuesto total
(7%). Al terminar el programa mostrará lo que el cliente debe pagar por su
compra (suma) y qué cantidad se corresponde con el IVA
"""
precio=float(input("Introduce el precio del producto: "))
valorTotal=0
iva=0
while precio>=0:
    valorTotal+=precio
    iva=iva+(valorTotal/7)*100
    precio=float(input("Introduce el precio de otro producto: "))
print(f"El precio total es: {valorTotal}€ y con IVA es {iva}€")