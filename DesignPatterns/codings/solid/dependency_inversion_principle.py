"""
        D — Dependency Inversion Principle (Inversão de Dependência)

Dependa de abstrações (interfaces), não de implementações concretas.
(Traduzindo: confie em “receber batata pronta”, não em como ela foi feita.)

Exemplo no código: Restaurante
"""


# Errado (classe depende direto da fritadeira):
# class Fritadeira:
#     def fritar(self):
#         print("Fritando batata")


# class Restaurante:
#     def __init__(self):
#         self.fritadeira = Fritadeira()

#     def servir_batata(self):
#         self.fritadeira.fritar()
#         print("Batata servida")


# Certo (classe depende da abstração Batata):
class Batata:
    def cozinhar(self):
        pass


class BatataFrita(Batata):
    def cozinhar(self):
        print("Fritando batata...")


class Restaurante:
    def __init__(self, batata: Batata):
        self.batata = batata

    def servir_batata(self):
        self.batata.cozinhar()
        print("Batata servida")
