# self equivalente ao this,aponta para a instancia da classe, tem que ser declarado no construtor
# O primerio parametro dos metodos é obrigatorio a ter o self, mesmo com parametro vazios
class Bicicleta:
    # Construtor
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim plim...")
        
    def parar(self):
        print("Bicicleta Parada")
        
    def correr(self):
        print("Correndo!")
    
    # Metodo para acessar informações da classe
    def __str__(self):
        return f"Nome da Classe: {self.__class__.__name__} \n Atributos: { ', '.join([ f'{elem[0]} = {elem[1]}' for elem in self.__dict__.items() ]) }"

    # Destrutor
    def __del__(self):
        print("Destruindo a Classe...")
    
b1 = Bicicleta("vermelha", "caloi", 2023, 1500)
b1.buzinar() # Bicicleta.buzinar(b1)
b1.parar()
b1.correr()
print(b1)

