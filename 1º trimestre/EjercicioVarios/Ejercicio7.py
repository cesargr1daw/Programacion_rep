"""7. Construye un programa que pinte todas las tablas de multiplicar del 1 al 10."""

for i in range(1,10+1):
    for j in range(1,10+1):
        print(f"{i}*{j}={i*j}")