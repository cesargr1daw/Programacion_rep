"""
10. Realizar un programa que nos pida un número n, y nos diga cuantos números
hay entre 1 y n que sean primos. Un número primo es aquel que sólo es
divisible por 1 y por él mismo. Ejemplo: Para n=8:
1->primo
2->primo
3->primo
4->no primo
5->primo
6->no primo
7->primo
8->no primo
Resultado del programa: Entre 1 y 8 hay 5 números primos.
"""
n=int(input("Cuantos n números quieres?: "))
contador_primos=0
#desde 1 hasta el número
for num in range(1, n+1):
    if num==1:
        print("1-->No es primo")  #1 se ha de tener en cuenta que no es primo ya que solo es divisible por él mismo, asi que se printa por pantalla
    #si es mayor que uno, que recorra los números desde 2 hasta el límite
    elif num>1:
        es_primo=True #iniciamos variable booleana en True para saber si es primo
        for i in range (2,num):
            if num%i==0: #si el número es divisible entre otro que no sea él mismo, no es primo
                print(f"{num}-->No es primo")
                es_primo=False #si no es primo, la variable pasa a tomar un valor False
                break #para que no repita el condicional en el mismo número
        if es_primo: #si la variable es_primo es cierta, se printa por pantalla y se suma 1 al contador
            print(f"{num}-->Es primo")
            contador_primos+=1 #si el número es primo, la variable contador_primos incrementa en 1
print(f"Entre 1 y {n} hay {contador_primos} números primos")
