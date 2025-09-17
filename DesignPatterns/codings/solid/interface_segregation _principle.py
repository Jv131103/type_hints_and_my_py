"""
        I — Interface Segregation Principle (Segregação de Interface)

Não obrigue uma classe a implementar métodos que ela não precisa.
(É tipo não obrigar o garçom a aprender a fritar batata.)

Exemplo no código: batata frita
"""

# Errado:
# class Cozinha:
#     def fritar(self): pass
#     def assar(self): pass
#     def servir(self): pass

# class Garcom(Cozinha):
#     def fritar(self): raise Exception("Não sei fritar!")
#     def assar(self): raise Exception("Não sei assar!")
#     def servir(self): print("Servindo batata")


# Certo (separa responsabilidades em interfaces pequenas):
class Fritar:
    def fritar(self): pass


class Servir:
    def servir(self): pass


class Garcom(Servir):
    def servir(self):
        print("Servindo batata")


class Fritadeira(Fritar):
    def fritar(self):
        print("Fritando batata")
