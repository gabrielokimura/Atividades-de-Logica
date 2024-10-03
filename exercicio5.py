def primo (n):
    x=n
    while (x>2):
        x=x-1
        if (n % x==0):
            return False
    return True
p=int(input("Digite um número qualquer"))
verifica=primo (p)
if (verifica==False):
    print ("Não é primo")
else:
    print("É primo")