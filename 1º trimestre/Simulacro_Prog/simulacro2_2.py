
print("*" * 60)
print("A) Añadir cliente")
print("B) Mostrar los % de clientes premium y normales: ")
print("C) Mostrar información de clientes premium")
print("D) Mostrar información de clientes normales")
print("E) Salir")
print("*" * 60)
opcion = input().upper()
premium = 0
normales = 0
clientesT = premium + normales
precio_maxCP = 0
precio_maxCN = 0
mejor_clienteP = ""
mejor_clienteN = ""
producto_caroP = ""
producto_caroN = ""
precioP = 0
precioN = 0

while opcion != "E":
    match opcion:
        case "A":
            vip = input("¿Desea ser Premium?: (S/N)").upper()
            print("Pulse E para salir")
            while vip != "E":
                if vip == "S" or vip == "N":
                    if vip == "S":
                        correo = input("Introduce el correo: ")
                        premium += 1
                        pedido = int(input("Introduce el codigo del articulo: "))
                        unidad = int(input("Indica cuántas unidades: "))
                        precio_unidad = float(input("Introduce el precio por unidad: "))
                        while pedido >= 0:
                            precioP += unidad * precio_unidad
                            if precio_unidad > precio_maxCP:
                                mejor_clienteP = correo
                                producto_caroP = pedido
                                precio_maxCP = precio_unidad
                            pedido = int(input("Introduce el codigo del articulo: "))
                            unidad = int(input("Indica cuántas unidades: "))
                            precio_unidad = float(input("Introduce el precio por unidad: "))
                    else:
                        correo = input("Introduce el correo: ")
                        normales += 1
                        pedido = int(input("Introduce el codigo del articulo: "))
                        unidad = int(input("Indica cuántas unidades: "))
                        precio_unidad = float(input("Introduce el precio por unidad: "))
                        while pedido >= 0:
                            precioN += unidad * precio_unidad
                            if unidad > producto_caroN:
                                mejor_clienteN = correo
                                producto_caroN = unidad
                            pedido = int(input("Introduce el codigo del articulo: "))
                            unidad = int(input("Indica cuántas unidades: "))
                            precio_unidad = float(input("Introduce el precio por unidad: "))
                vip = input("¿Desea ser Premium?: (S/N)").upper()
                print("Pulse E para salir")
        case "B":
            clientesT = premium + normales
            porc_Premium = (premium * 100) / clientesT if clientesT > 0 else 0
            porc_Normales = (normales * 100) / clientesT if clientesT > 0 else 0
            print(f"Hay {porc_Premium}% de usuarios premium y {porc_Normales}% de usuarios normales")
        case "C":
            print(f"Mejor cliente premium: {mejor_clienteP}")
            print(f"Producto más caro comprado por cliente premium: {producto_caroP}")
            print(f"Precio máximo pagado por cliente premium: {precio_maxCP}")
        case "D":
            print(f"Mejor cliente normal: {mejor_clienteN}")
            print(f"Unidades más compradas por cliente normal: {producto_caroN}")
            print(f"Precio total pagado por cliente normal: {precioN}")

    print("*" * 60)
    print("A) Añadir cliente")
    print("B) Mostrar los % de clientes premium y normales: ")
    print("C) Mostrar información de clientes premium")
    print("D) Mostrar información de clientes normales")
    print("E) Salir")
    print("*" * 60)
    opcion = input().upper()
