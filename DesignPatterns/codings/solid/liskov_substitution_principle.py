"""
            L — Liskov Substitution Principle (Substituição de Liskov)

Se uma classe herda de outra, ela deve poder ser usada no lugar da mãe sem
quebrar nada. (Em outras palavras: filho não pode fazer papelão na frente da
mãe)

Exemplo no código: batata assada vs frita
"""


# Errado (filho não respeita o contrato: não frita!):
# class Batata:
#     def cozinhar(self):
#         print("Fritando batata...")


# class BatataAssada(Batata):
#     def cozinhar(self):
#         raise Exception("Eu não sei fritar!")  # quebrou a regra!


# Certo (cada um cozinha à sua maneira, mas todos respeitam o "cozinhar"):
class Batata:
    def cozinhar(self):
        pass


class BatataFrita(Batata):
    def cozinhar(self):
        print("Fritando batata...")


class BatataAssada(Batata):
    def cozinhar(self):
        print("Assando batata...")
