
ENERGIA_INSETO = 8000

def nvl_energia(n):
    if n <= ENERGIA_INSETO:
        print("Inseto!")
    else:
        print("Mais de 8000!")

C = int(input()) 
for i in range (C):
    n = int(input())
    if (n >= 100) and (n <= 100000):
        nvl_energia(n)
    else:
        print("Erro - 'n' Invalido" )