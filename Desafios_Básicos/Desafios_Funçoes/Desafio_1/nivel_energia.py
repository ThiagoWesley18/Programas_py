

def nvl_energia(n):
    if n <= 8000:
        return "Inseto!"
    elif n > 8000:
        return "Mais de 8000!"

C = abs(int(input())) 
for i in range (C):
    n = int(input())
    if (n >= 100) and (n <= 100000):
        print(nvl_energia(n))
    else:
        print("Erro - 'n' Invalido" )