"""
        S — Single Responsibility Principle (Responsabilidade Única)

Cada classe/função deve ter uma só tarefa.

Exemplo no código: batata frita
"""

# Errado (a classe faz tudo: cozinha e serve batata):
# class Batata:
#     def fritar(self):
#         print("Fritando batata...")

#     def servir(self):
#         print("Servindo batata no prato")


# Certo (uma cuida da fritura, outra de servir):
class Fritadeira:
    def fritar(self):
        print("Fritando batata...")


class Garcom:
    def servir(self):
        print("Servindo batata no prato")
