
# ------------------Funçao com default-------------------- #
def exibir_mensagem(nome="anonimo"):
    print(f"ola {nome}")

# -----------Return pode retornar mais de um valor------------ #
def sucessor_antecessor(valor):
    sucessor = valor+1
    antecessor = valor-1
    return sucessor, antecessor


exibir_mensagem("thiago")# exibir_mensagem(nome="thiago") - é mais seguro!
exibir_mensagem()
print("\n")

sucessor, antecessor = sucessor_antecessor(0)# Retorna uma tupla ou ja faz a atribuição para cada variavel
print("retorno: ", sucessor,antecessor)
print("\n")

# --------------Arquementos com tuplas e dic-------------- #
# *arq - tuplas
# **arqs - dic
def texto(titulo, *arg, **arg2):
    texto = "\n".join(arg)
    dados = "\n".join( f"{chave} = {valor}" for chave,valor in arg2.items() )
    print(f"{titulo} \n\n {texto} \n\n {dados}")

texto("Thiago", "linha1", "linha2", "linha3", Autor="Thiago", Ano=2023)
print("\n")

# ---------------Positional-only-------------- #
# Antes da / os parametros sao apenas por posição
# Depois de * os parametros devem ter chave=valor
def param(nome, sobrenome, /, *, idade,):
    print(f"{nome} {sobrenome} tem {idade} anos")

param("thiago", "wesley", idade=26)# Chamada obrigatoria por causa do positional-only
print("\n")

# ---------------Função de primeira classe --------------- #
# Passando uma funçao como parametro (callback)
def funçao_interna():
    return "Executou na função Interna!"
def funçao_externa(funçao):
    print(f"Callbeck - {funçao()}")
funçao_externa(funçao_interna)


# Atribuindo uma função a uma variavel
executa = funçao_interna
print("Executando na variavel - ", executa())
print("\n")

# --------------Escopo Glabal-------------- #
# Não é recomendavel
valor = 2000
def incrementa(salario):
    global valor 
    valor += salario
    return valor
print(f"Incremeto - {incrementa(1000)} \n valor global - {valor}")

