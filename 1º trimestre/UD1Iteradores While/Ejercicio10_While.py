"""
10. Crea un programa que genere dos números al azar entre el 0 y el 100, y pida al
usuario que calcule e introduzca su suma. Si la respuesta no es correcta,
deberá volver a pedirla tantas veces como sea necesario hasta que el usuario
acierte. Pista: usa la función random.randint(0, 100)
"""
import random
num_alt1=random.randint(0,100+1)
num_alt2=random.randint(0,100+1)
print(f"¿Cual es la respuesta de {num_alt1}+{num_alt2}?")
sol=num_alt1+num_alt2
respuesta=int(input("La respuesta es: "))
while sol!=respuesta:
    respuesta=int(input("Respuesta incorrecta, intentalo de nuevo. La respuesta correcta es: "))