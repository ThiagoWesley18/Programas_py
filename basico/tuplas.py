# tuplas sao imutaveis, ao contrario das listas
# sao criadas atraves de valores separados por virgula entre parenteses
# guarda objetos
# mesmos metodos da lista

frutas = ("maçã", "laranja", 12,)
letras = tuple("python")

print(frutas[0])
print(frutas[-1])

matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)

print(matriz[2][2])