# set é um conjunto de numeros não repeditos
# nao suporta indexação nem fatiamento

print(set([1 ,2, 2, 3]))# cria um conjunto de numeros nao repetidos

# Convertendo set em lista
conjunto = {2, 3, 4}
lista = list(conjunto)
print(lista[0])

# pecorrendo set(conjunto)
for i in conjunto:
    print(i, end=" ")

# Operação de Conjuntos
num1 = {1, 2, 3}
num2 = {3, 5, 6}

print("\n")
print("União: ", num1.union(num2))
print("Interseção: ", num1.intersection(num2))
print("Diferença: ",num1.difference(num2))
print("Elementos que não estão na interseção: ", num1.symmetric_difference(num2))
print("Num1 pertecem a Num2? ",num1.issubset(num2))
print("num1 e num2 sao disjuntos? ",num1.isdisjoint(num2))
num1.add(4)# Adiciona elemento 4 no conjunto
print("Copia de num1: ", num1.copy())
num1.discard(4)# Elimina um valor do cojunto, se o elemento nao existir, nao faz nada e continua o programa
num1.remove(1)# Mesmo que o discard, porem se o elemeto a ser removido nao existir retorna um erro.
num1.pop()# Retira o primeiro elemento do conjunto, nao aceita parametros, ao contrario das listas e tuplas
num1.clear()# Conjunto vazio
print("tamnaho de num1: ", len(num1))