print("*"*60)
print("A) Añadir cliente")
print("B) Mostrar los % de clientes premium y normales: ")
print("G) Salir")
print("*"*60)
opcion = input().upper()
premium = 0
normales = 0

while opcion != "G":
    match opcion:
        case "A":
            vip = input("¿Desea ser Premium?: (S/N)").upper()
            print("Pulse G para salir")
            while vip != "G":
                if vip == "S" or vip == "N":
                    if vip == "S":
                        correo = input("Introduce el correo: ")
                        premium += 1
                    else:
                        correo = input("Introduce el correo: ")
                        normales += 1
                vip = input("¿Desea ser Premium?: (S/N)").upper()
                print("Pulse G para salir")
        case "B":
            clientesT = premium + normales  # Debes calcular clientesT aquí
            if clientesT > 0:
                porc_Premium = (premium * 100) / clientesT
                porc_Normales = (normales * 100) / clientesT
                print(f"Hay {porc_Premium}% de usuarios premium y {porc_Normales}% de usuarios normales")
            else:
                print("No hay clientes registrados.")
    
    print("*"*60)
    print("A) Añadir cliente")
    print("B) Mostrar los % de clientes premium y normales: ")
    print("G) Salir")
    print("*"*60)
    opcion = input().upper()
