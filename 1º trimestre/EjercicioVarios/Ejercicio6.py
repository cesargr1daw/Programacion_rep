"""
6. Construye un programa que te pida un nombre. Sólo si el nombre introducido
se corresponde con el del usuario a logar, nos pide la clave de dicho usuario.
Si ambas cosas son correctas, imprime “Usuario logado correctamente”. Si
no se corresponde seguirá pidiéndonos el nombre de la misma forma que si
la clave no se corresponde.
"""
user=input("Introduce el nombre de usuario: ")
userR="usuario"
passwordR="contraseña"
while userR!=user:
    user=input("Introduce el nombre de usuario: ")
while user==userR:
    password=input("Introduzca su contraseña: ")
    while passwordR!=password:
        user=input("Introduce el nombre de usuario: ")
print("Usuario logado correctamente")


