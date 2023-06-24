
N = int(input())

while(N > 0):
    
    a, b = input().split()
    

    # strings com menos de 1000 caracteres
    if (0 < len(a) <= 1000)  and (0 < len(b) <= 1000):

        if len(a) >= len(b):
            string = a[len(a) - len(b) : ]
            if string == b:
                print("encaixa")
            else:
                print("nao encaixa")
        else:
            print("nao encaixa")  
    N -= 1 




