print("*"*60)
print("A) Añadir cliente")
print(f"B) Mostrar los % de clientes premium y normales: ")
print("G) Salir")
print("*"*60)
opcion=input().upper()
premium=0
normales=0
clientesT=premium+normales
mejor_clienteP=""
mejor_clienteN=""
producto_caroP=""
precio_maxCP=0
precio_maxCN=0
art_maxCaroP=0
precio_TotalP=0
precio_TotalN=0
cod_art_maxCaroP=""
prod_max_vendido=0
mas_vendido=""
while opcion!="G":
    match opcion:
        case "A":
                vip=input("¿Desea ser Premium?: (S/N)").upper()
                print("Pulse G para salir")
                while vip!="G":
                    if vip=="S" or vip=="N":
                        if vip=="S":
                            correo=input("Introduce el correo: ")
                            premium+=1
                            pedido=int(input("Introduce el codigo del articulo: "))
                            unidad=int(input("Indica cuántas unidades: "))
                            precio_unidad=float(input("Introduce el precio por unidad: "))
                            while pedido>=0:
                                pedido=input("Introduce el codigo del articulo: ")
                                unidad=int(input("Indica cuántas unidades: "))
                                precio_unidad=float(input("Introduce el precio por unidad: "))
                                precio_TotalP+=(unidad*precio_unidad)
                                if precio_maxCP<(precio_TotalP):
                                    mejor_clienteP=correo
                                    producto_caroP=unidad
                                    precio_maxCP=precio_TotalP
                                if art_maxCaroP<precio_unidad:
                                    cod_art_maxCaroP=pedido
                                    precioP=precio_unidad
                                 
                        else:
                            correo=input("Introduce el correo: ")
                            normales+=1
                            pedido=int(input("Introduce el codigo del articulo: "))
                            unidad=int(input("Indica cuántas unidades: "))
                            precio_unidad=float(input("Introduce el precio por unidad: "))
                            while pedido>=0:
                                pedido=input("Introduce el codigo del articulo: ")
                                unidad=int(input("Indica cuántas unidades: "))
                                precio_unidad=float(input("Introduce el precio por unidad: "))
                                precio_TotalN+=(unidad*precio_unidad)
                                if prod_max_vendido<unidad:
                                    mas_vendido=pedido
                                if precio_maxCP<(precio_TotalP):
                                    mejor_clienteN=correo
                                    producto_caroN=unidad
                                    precio_maxCN=precio_TotalN


                    vip=input("¿Desea ser Premium?: (S/N)").upper()
                    print("Pulse G para salir")
        case "B":
            porc_Premium=premium*100/clientesT
            porc_Normales=normales*100/clientesT
            print(f"Hay {porc_Premium}% de usuarios premium y {porc_Normales}% de usuarios normales")
        case "C":
            print(porc_Premium)
            print(mejor_clienteP)
            print(producto_caroP)
        case "D":
            print(porc_Normales)
            print(mas_vendido)
        case "E":
            if precio_maxCN>precio_maxCP:
                print(mejor_clienteN)
                print(precio_maxCN)
            else:
                print(mejor_clienteP)
                print(precio_maxCP)
    print("*"*60)
    print("A) Añadir cliente")
    print("B) Mostrar los % de clientes premium y normales: ")
    print("G) Salir")
    print("*"*60)
    opcion=input().upper()