def parimpar (n1):
    if (n1 % 2 == 0):
        return True
    else:
        return False
    
n1=int(input("Digite um número qualquer"))
verificação = parimpar (n1)
if (verificação==True):
    print ("É par")
else:
    print("É ímpar")
    

    