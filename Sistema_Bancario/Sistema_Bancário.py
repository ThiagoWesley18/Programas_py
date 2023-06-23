


saldo = 0
LIMTE_SAQUE = 500.00
quantidade_saque = 0
extrato = ""

while True:
    opcao = input(
        """
        [D] - Depósito
        [S] - Saque
        [E] - Extrato
        [Q] - Sair

        """
    ).upper()

    if opcao == "D":
        valor = float(input("Digite o Valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R${valor:.2f}\n"
        else:
            print("Valor inválido!")
    
    elif opcao == "S":
        if quantidade_saque <= 3:
            valor_de_saque = float(input("Digite o valor a ser sacado: "))
            if (valor_de_saque <= LIMTE_SAQUE):
                if valor_de_saque <= saldo:
                    saldo -= valor_de_saque
                    extrato += f"Saque de R${valor_de_saque:.2f}\n"
                    quantidade_saque += 1
                else:
                    print("Saldo Insuficiente!")
            else:
                 print("Limite de saque atingido!")
        else:
            print("Quantidade de saque atingido!\n")

    elif opcao == "E":
        print("\n\n----------Extrato----------\n")
        if extrato == "":
            print("Sem Movimenteções!")
        else:
            extrato += f"Valor na conta: {saldo:.2f}\n"
            print(extrato)
    
    elif opcao == "Q":
        print("Fim da Operação!")
        break
    else:
        print("Opção Invalida!d")

    

