class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa...")

avestruz = Avestruz()
pardal = Pardal()
pardal.voar()
avestruz.voar()
