"""
9. Construye un programa que pida al usuario una contraseña, de forma
repetitiva mientras que no introduzca "1234". Cuando finalmente escriba la
contraseña correcta, se le dirá "Bienvenido" y terminará el programa.
"""
contraseña=input("Introduce la contraseña: ")
while contraseña!="1234":
    contraseña=input("Contraseña incorrecta. Introduce la contraseña de nuevo: ")
print("Bienvenido")