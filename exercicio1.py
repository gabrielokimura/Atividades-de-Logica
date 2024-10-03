def segundograu (a,b,c):
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    return x1, x2

a=float(input("Digite o valor de a"))
b=float(input("Digite o valor de b"))
c=float(input("Digite o valor de c"))
if (b**2-4*a*c<0):
    print("Não existe solução nos números reais")
else:
    solução=segundograu (a,b,c)
    print(solução)