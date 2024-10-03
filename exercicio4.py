def fatorial (fat):
    x=fat
    cont=1
    while (cont!=x):
        fat=fat*cont
        cont=cont+1
    return (fat)

sla=int(input("Digite um número qualquer"))
result= fatorial (sla)
print(result)
