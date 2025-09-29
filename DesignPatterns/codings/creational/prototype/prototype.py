"""
Especificar os tipos de objetos a serem criados usando uma
instância-protótipo e criar novos objetos pela cópia desse protótipo
---
Quais objetos são copiados com o sinal de atribuição?
    *

    Objetos imutáveis são copiados e mutáveis são referenciados
"""

from __future__ import annotations

from copy import deepcopy
from typing import List


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self):
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":
    joao = Person("João", "Justino")
    endereco_joao = Address("Rua X", "1444")

    joao.add_address(endereco_joao)
    print(joao)

    esposa_joao = joao.clone()
    esposa_joao.firstname = "Ninguém"
    print(esposa_joao)
