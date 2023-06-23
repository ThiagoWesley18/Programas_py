
# acessa a os indices atraves do enumerate - retorna o indice e o valor
carro = ["onix", "gol", "polo"]
for indice,valor in enumerate(carro):
    print(f"indice: {indice} - valor: {valor}")
print("\n\n")

# Filtrar Lista
numeros = [1, 3, 2, 34, 57, 8, 9, 1020, 3]
numero_par = []

numero_par =[num for num in numeros if num % 2 == 0 ]# IF ternario com for
quadrados = [num**2 for num in numeros]# melhor forma de filtrar a Lista

#print(f"\nLista dos numeros pares: {numero_par}\n")
#print(f"\nLista dos quadrados dos numeros: {quadrados}\n")

# Metodos Principais
print("Lista Principal: ", numeros)
numeros.append("string")# adiciona na ultima posiçao da lista
lista2 = numeros.copy()# cria uma copia da lista
print("Qtd de elementos 3: ",numeros.count(3))# retonar a quandidade do objeto na lista
numeros.extend([2, 78, 90])# adiciona uma lista em outra
print("Lista extendida: ",numeros)
print("Indice do elemento 3: ",numeros.index(3))# retorna o primeiro indice do valor passado (0)
print("Retira o elemento de indice 0 da lista: ",numeros.pop(0))# retira o elemento de indice 0 da lista
numeros.remove("string")# remove o elemento "string" da lista
print("lista sem o elemeto 'string': ",numeros)
numeros.reverse()# inverte lista
print("lista revertida: ", numeros)
numeros.sort()# ordena lista, se for apens strings ordena por ordem alfabetica
numeros.sort(reverse=True)# ordena de forma decrescente
lista_string =  ["string", "palavra"]
lista_string.sort(key = lambda x: len(x),reverse=True)# ordena lista_string pelo tamnaho das palavras atraves da função anonima lambda
print("lista ordenada pelo tamnaho da string: ",lista_string)
print("tamnaho da lista_string: ",len(lista_string))# retorna o tamhanho da






numeros.clear()# lista vazia