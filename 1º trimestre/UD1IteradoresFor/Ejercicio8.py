"""
8. Diseñar un programa que muestre el producto de los 10 primeros números
impares.
"""
recorre=10
total=1
for i in range (1,22,2):
    print(f"{total}*{i}")
    total*=i
    print(total)