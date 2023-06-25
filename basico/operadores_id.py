
# Operadores de Identidade - se os objetos estao na mesma regiao de memoria
nome_curso = "Engenharia da computação"
curso = nome_curso

print(nome_curso is curso) 
print(nome_curso is not curso)

# Operadores de Associação - se os objetos estao em uma sequencia
frutras = ["maça", "abacate","limao"]


print("maça" in frutras)
print("maça" not in frutras)
print("Engenharia da computação" in curso)