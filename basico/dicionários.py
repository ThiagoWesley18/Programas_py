# Dicionario é um conjunto nao ordenado de chave-valor
# Chave tem que ser um obj imutavel(tuplas,strings,numeros,etc)
# Pode armazenar qualquer tipo de obj

# Criar 
pessoa = { "nome" : "Thiago" , "idade": 26 }
individuo = dict( nome="Thiago" , idade=26 )
cadastro = {
    "id_1" : { "nome":"thiago" , "idade":26 },
    "id_2" : { "nome":"Mateus" , "idade":21 }
}

# Acessar valor e modificar
pessoa["nome"] =  "Thiago Wesley" # Modifica valor da chave existente
pessoa["telefone"] = "9999-9999" # Adiciona nova chave-valor
print(cadastro["id_1"]["nome"])
print("\n")
for chave,valor in pessoa.items():
    print(chave,valor)


# Metodos de dicionarios
print("\n-----Principais Métodos-----")
individuo.clear()# Dicionario Vazio
print("Copia de pessoas: ",pessoa.copy())# Retorna uma copia
print("Dicionario criado com chaves: ", dict.fromkeys(["endereço", "CPF"], "vazio"))# Retorna um novo dicionario com as chaves criadas com valor "vazio"
print("Retorna o valor da chave: ",pessoa.get("nome"))# Retorna o valor da chave, se nao existir retorna none
print("Retona chave:valor - ", pessoa.items())# Retorna uma LISTA de TUPLAS com a (chave,valor)
print("Chaves: ", pessoa.keys())# Retorna uma LISTA com as chaves
print("valor: ", pessoa.values())# Retorna uma LISTA com os valores
print("pop: ", pessoa.pop("idade", "Chave nao existe!"))# Retira e retorna a (chave:valor) do dicionario, senao achar retorna o segundo parametro
print("setdefault: ", pessoa.setdefault("CPF","24343243"))# Adiciona uma (chave:valor) e retorna, se existir retorna a existente e nao altera

del pessoa["telefone"]# retira um objeto, se nao existir da erro
print("Del telefone: ", pessoa)

teste = {1:"teste"}
print("popitem: ",teste.popitem())# retira elementos do dic na sequencia, se nao houver elementos da erro

contatos = {"nome": "Guilherme", "telefone": "3333-2221"}
print("Contatos: ",contatos)
contatos.update({"nome": "Gui"})# Atualiza o dic com o novo dic passado, se a chave nao existir é criada
print("Update Contatos: ", contatos)


