
T = input("-----Escreva sua mensagem-----\n")
tam = len(T)

if (tam >= 1) and (tam <= 500):
    if tam <= 140:
        print("TWEET")
    else:
        print("MUTE")
