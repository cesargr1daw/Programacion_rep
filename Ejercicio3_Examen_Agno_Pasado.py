tamagnoEmpresa = int(input("Introduce el número de trabajadores que tiene la empresa: "))
python = 0
java = 0
hombresP = 0
mujeresP = 0
hombresJ = 0
mujeresJ = 0
edadTotalP = 0
edadTotalJ = 0

for i in range(tamagnoEmpresa):
    lenguaje = input("Introduce el lenguaje que usas (python o java): ").lower()
    while lenguaje != "python" and lenguaje != "java":
        lenguaje = input("Introduce un lenguaje válido (python o java): ").lower()

    sexo = input("Introduce si eres hombre o mujer (H o M): ").lower()
    edad = int(input("Introduce tu edad: "))
    
    if lenguaje == "python":
        edadTotalP += edad
        if sexo == "h":
            hombresP += 1
        else:
            mujeresP += 1
        python += 1
    elif lenguaje == "java":
        edadTotalJ += edad
        if sexo == "h":
            hombresJ += 1
        else:
            mujeresJ += 1
        java += 1

print(f"El {python*100/tamagnoEmpresa} de empleados utiliza python, de los cuales {hombresP} son hombres y {mujeresP} mujeres y su edad media {edadTotalP/(mujeresP+hombresP)}")
print(f"El {java*100/tamagnoEmpresa} de empleados utiliza java, de los cuales {hombresJ} son hombres y {mujeresJ} mujeres y su edad media {edadTotalJ/(mujeresJ+hombresJ)}")
