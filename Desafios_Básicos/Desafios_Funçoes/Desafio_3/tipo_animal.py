a = input() 
b = input() 
c = input() 



if a == 'vertebrado': 
    if b == "ave":
        if c == "carnivoro":
            print("aguia")
        elif c == "onivero":
            print("pomba")
        else:
            print("Erro!")
    elif b == "mamífero":
        if c == "onivero":
            print("homem")
        elif c == "herbivoro":
            print("vaca")
    else:
        print("Erro")
   
elif a == 'invertebrado':
    if b == "inseto":
        if c == "hematofago":
            print("pulga")
        elif c == "herbivoro":
            print("lagarta")
        else:
            print("Erro!")
    elif b == "anelideo":
        if c == "hematofago":
            print("sanguessuga")
        elif c == "onivero":
            print("minhoca")
    else:
        print("Erro")