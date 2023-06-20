

nome = "Thiago Wesley"
curso = "Python"
print(f"\n---------Este é um codigo de exemplos de {nome} do curso {curso}---------\n")

## Metodos básicos
curso = "pYtHon"
print("1 - " + curso.lower()) # retorna minusculas
print("2 - " +curso.upper()) # retorna maiscula
print("3 - " +curso.title()) # retorna valor da variavel

curso = "  pYtHon "
print("4 - " +curso.strip()) # retorna sem os espaços

curso = "python"
print("5 - " +curso.center(10,"#"))# retorna a string centralizada entre "#" e com tamanho 10
print("6 - " + ".".join(curso))# retorna uma string separada por "."

## Interpolação de Variaveis
PI = 3.14159
print(f"7 - valor de pi: {PI:.2f}")# com duas casas decimais
print(f"8 - valor de pi: {PI:10.2f}")# com duas casas decimais e pulanda 10 espaços

## Fatiamento de String
nome = "Thiago Wesley Cunha de Oliveira"

print(f"9 -  {nome[0]}")
print(f"10 -  {nome[:6]}")# inicio ate posiçao 6
print(f"11 -  {nome[7:]}")# posição 7+1 ate o final da string
print(f"12 -  {nome[7:13]}")# posiçao 7+1 ate 13
print(f"13 -  {nome[::-1]}")# -1 faz espelhar a string

mensagem = """ 
Ola, meu nome é Thiago,
faço parte do curso de python.

att.
Thiago Wesley
"""
print(mensagem)