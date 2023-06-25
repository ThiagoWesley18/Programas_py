
def deposito(valor,saldo,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R${valor:.2f}\n"
    else:
        print("Valor inválido!")
        return saldo, extrato
    return saldo, extrato

def saque(*, quantidade_saque,saldo,extrato):
    if quantidade_saque > 0:
        valor_de_saque = float(input("Digite o valor a ser sacado: "))
        if (valor_de_saque <= LIMTE_SAQUE):
            if valor_de_saque <= saldo:
                saldo -= valor_de_saque
                extrato += f"Saque de R${valor_de_saque:.2f}\n"
                quantidade_saque -= 1
            else:
                print("Saldo Insuficiente!")
                return saldo, extrato, quantidade_saque
        else:
            print("Limite de saque atingido!")
            return saldo, extrato, quantidade_saque
    else:
         print("Quantidade de saque atingido!\n")
         return saldo, extrato, quantidade_saque
    return saldo, extrato, quantidade_saque

def mostrar_extrato(saldo, /, *, extrato):
    print("\n\n----------Extrato----------\n")
    if extrato == "":
        print("Sem Movimenteções!")
    else:
        extrato += f"Valor na conta: {saldo:.2f}\n"
        print(extrato)

def criar_usuario(nome,data_nascimento,cpf,endereço):
    lista = [ {"nome": nome, "data" : data_nascimento, "cpf" : cpf, "endereço" : endereço} ]
    return lista

def exibir_clientes(clientes):
    texto = [f"{elem[0]} : {elem[1]}" for elem in clientes]
    for i in texto:
        print("Dados do clitente: ",i)
    
def cpf_isCliente(cpf, clientes):
    if clientes != []:
        result = [True for elem in clientes  if elem["cpf"] == cpf ]
        return True in result
    else:
        return False

def buscar_usuario(cpf,cliente):
    if cliente != []:
        result = [elem for elem in cliente  if elem["cpf"] == cpf ]
        return result[0]
    else:
        return None


def criar_conta(ag, numero_conta, clientes):
    cpf = input("Informe o CPF(apenas numeros): ")
    if cpf_isCliente(cpf, clientes):
        cliente = buscar_usuario(cpf,clientes)
        if cliente != None:
            conta = {"agencia": ag , "Numero da conta": numero_conta, "Cliente: " : cliente}
            return conta
        else:
            print("Erro na busca!")
    else:
        print("CPF não cadastrado!")

def main():
    saldo = 0
    LIMTE_SAQUE = 500.00
    AGENCIA = "0001"
    quantidade_saque = 3
    extrato = ""
    clientes = []
    conta = []

    while True:
        opcao = input(
            """
            [D] - Depósito
            [S] - Saque
            [E] - Extrato
            [U] - Cliente
            [C] - Conta
            [Q] - Sair

            """
        ).upper()

        if opcao == "D":
            valor = float(input("Digite o Valor a ser depositado: "))
            saldo, extrato = deposito(valor,saldo,extrato)  
        
        elif opcao == "S":
            saldo, extrato, quantidade_saque = saque(quantidade_saque=quantidade_saque,saldo=saldo,extrato=extrato)

        elif opcao == "E":
            mostrar_extrato(saldo,extrato=extrato)

        elif opcao == "U":
            opçao_cliente = input(
                """
                #----------Area do Cliente--------#
                [C] - Criar novo cliente
                
                """
            ).upper()
            if opçao_cliente == "C":
                cpf = input("Digite seu CPF(apenas numeros): ")
                if not(cpf_isCliente(cpf, clientes)):
                    nome = input("Digite seu nome: ")
                    data_nascimento = input("Digite sua data de nascimento: ")
                    endereço = input("Edereço(logradouro - bairro - cidade/UF): ")
                    clientes.extend(criar_usuario(nome,data_nascimento,cpf,endereço))
                else:
                    print("CPF ja Exste!")
            else:
                print("Opção invalida!")

        elif opcao == "C":
            numero_conta = len(conta) + 1
            if clientes != []:
                conta.append(criar_conta(AGENCIA, numero_conta, clientes))
            else:
                print("Sem clientes cadastrados!")
            print(conta)
        
        elif opcao == "Q":
            print("Fim da Operação!")
            break
        else:
            print("Opção Invalida!")

main()    

