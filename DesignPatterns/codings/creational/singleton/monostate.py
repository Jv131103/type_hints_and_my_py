"""
Monostate (ou Borg) - É uma variação do Singleton proposto por Alex Martelli
que tem a itenção de garantir que o estado do objeto seja igual para todas as
instâncias
"""


class StringReprMixing:
    def __str__(self) -> str:
        params = ', '.join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__} ({params})"

    def __repr__(self) -> str:
        return self.__str__()


class MonoStateSimple(StringReprMixing):
    _state = {
        'x': 10,
        'y': 20,
    }

    def __init__(self, nome=None, sobrenome=None) -> None:
        self.x = 0
        self.y = 0
        self.__dict__ = self._state

        if nome:
            self.nome = nome

        if sobrenome:
            self.sobrenome = sobrenome


if __name__ == "__main__":
    m1 = MonoStateSimple(nome="Leo")
    m1.x = 20  # Vai alterar todos os outros objetos
    m2 = MonoStateSimple(sobrenome="Fizza Now")
    print(m1)
    print(m2)
