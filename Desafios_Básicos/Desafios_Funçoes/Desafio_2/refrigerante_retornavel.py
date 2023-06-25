def numero_garrafas(n,k):
   ganha = 0 
   total = 0
   if n >= k:
        # Garrafas ganhas com a promoção
        ganha = n//k
        # Quantidade de vezes que a promoção foi aplicada
        if (n/k) - (n//k) != 0:
            perda = n//k
        total = (n-(k*perda)) + ganha
        print(total)
   else:
       print(n)


T = int(input())
if (T >= 1) and (T <= 10000):
    for i in range(T):
        n,k = input().split()
        n,k = [int(n),int(k)]
        if (k >= 1) and (n <= 10000):
            numero_garrafas(n,k)

