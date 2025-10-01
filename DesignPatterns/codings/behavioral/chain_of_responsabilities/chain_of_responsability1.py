"""
Chain of responsability (COR) é um padrão comportamental que tem a
itenção de evitar o acoplamento do remetente de uma solicitação ao seu
receptor, ao dar a mais de um objeto a oprtunidade de tratar a solicitação.

Encadear os objetos receptores passando a solicitação ao longo da cadeia até
que um objeto a trate
"""


def handler_ABC(letter: str) -> str:
    letters = ['A', 'B', 'C']

    if letter in letters:
        return f"handler_ABC: conseguiu tartar o valor {letter}"
    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = ['D', 'E', 'F']

    if letter in letters:
        return f"handler_DEF: conseguiu tartar o valor {letter}"
    return handler_unsolve(letter)


def handler_unsolve(letter: str) -> str:
    return f"handlers não encotraram {letter}"


print(handler_ABC("A"))
print(handler_ABC("B"))
print(handler_ABC("C"))
print(handler_ABC("D"))
print(handler_ABC("E"))
print(handler_ABC("F"))
print(handler_ABC("G"))
print(handler_ABC("H"))
print(handler_ABC("I"))
