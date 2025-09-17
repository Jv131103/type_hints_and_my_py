"""
            O — Open/Closed Principle (Aberto/Fechado)

Seu código deve estar aberto para extensão (dá pra adicionar coisas novas),
mas fechado para  modificação (não precisa mudar o que já funciona).

Exemplo no código: molhes de batata
"""


# Errado (precisa mudar o código sempre que adicionar molho novo):
# def servir_molho(tipo):
#     if tipo == "ketchup":
#         return "Ketchup"
#     elif tipo == "maionese":
#         return "Maionese"


# Certo (a função aceita novos molhos sem precisar ser mexida):
class Molho:
    def servir(self):
        pass


class Ketchup(Molho):
    def servir(self):
        return "Ketchup"


class Maionese(Molho):
    def servir(self):
        return "Maionese"


def servir_molho(molho: Molho):
    return molho.servir()
