tamañoEmpresa=int(input("Introduce el número de trabajadores tiene la empresa: "))
python=0
java=0
totalP=tamañoEmpresa
while 0<totalP:
    lenguaje=input("Introduce el lenguaje que usas: ")
    lenguaje=lenguaje.islower()
    while not(lenguaje=="python" or lenguaje=="java"):
        lenguaje=input("Introduce el lenguaje que usas: ")
        lenguaje=lenguaje.islower()
    match lenguaje:
        case "python":
            hombresP=0
            mujeresP=0
            edadTotal=0
            sexo=input("Introduce si eres hombre o mujer (H o M): ")
            sexo=sexo.islower()
            edad=int(input("Introduce tu edad:"))
            edadTotal+=edad
            if sexo=="h":
                hombresP+=1
            else:
                mujeresP+=1
            python+=1

        case "java":
            hombresJ=0
            mujeresJ=0
            edadTotal=0
            sexo=input("Introduce si eres hombre o mujer (H o M): ")
            sexo=sexo.islower()
            edad=int(input("Introduce tu edad:"))
            edadTotal+=edad
            if sexo=="h":
                hombresJ+=1
            else:
                mujeresJ+=1
            java+=1
    totalP-=1

print(f"El {python*100/tamañoEmpresa} de empleados utiliza python, de los cuales {hombresP} son hombres y {mujeresP} mujeres y su edad media {edadTotal/(mujeresP+hombresP)}")
print(f"El {java*100/tamañoEmpresa} de empleados utiliza java, de los cuales {hombresJ} son hombres y {mujeresJ} mujeres y su edad media {edadTotal/(mujeresJ+hombresJ)}")
