
# IF
saldo = 2000
cheque_especial = 100

saque = float(input("Valor do saque: "))

if saque <= saldo:
    print("Realizando Saque")
    saldo -= saque
elif saque <= (saldo + cheque_especial):
    print("Realizando Saque com Cheque Especial")
    saldo, cheque_especial = [0, (saldo + cheque_especial) - saque]
else:
    print("saldo Insuficiente")


## IF ternarrio
status = "sucesso" if saque <= saldo else "conta no Cheque Especial"
print(status)

# For

VOGAIS = "AEIOU"

for letra in VOGAIS:
    print(letra)

#print(list(range(1,4,1)))

for i in range(0,51,5):
    print(i, end=" ")



