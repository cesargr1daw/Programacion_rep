base=int(input("Introduce la raíz: "))
expt=int(input("Introduce el exponente: "))
resl=1
while expt>0:
    resl*=base
    expt=expt-1
print(resl)