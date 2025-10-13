"""
Flyweight é um padrão de projeto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades
de objetos de forma granular.

Só use o Flyweight quanto TODAS as condições
a seguir forem verdadeiras:

- uma aplicação utiliza uma grande quantidade de
objetos;
- os custos de armazenamento são altos por causa
da grande quantidade de objetos;
- a maioria dos estados de objetos podem se tornar
extrínsecos;
- muitos objetos podem ser substituídos por poucos
objetos compartilhados;
- a aplicação não depende da identidade dos objetos.

Importante:
- Estado intrínseco é o estado do objeto que não muda,
esse estado deve estar dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda,
esse estado pode ser movido para fora do objeto
flyweight;

Dicionário:
Intrínseco - que faz parte de ou que constitui a
essência, a natureza de algo; que é próprio de
algo; inerente.
Extrínseco - que não pertence à essência de algo;
que é exterior.
"""
from __future__ import annotations

from typing import Dict, List


class Client:
    '''CONTEXT'''
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._addresses: List = []

        # Extrinsic address data
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    """Flyweight"""
    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_detail: str):
        print(
            self._street,
            address_number,
            self._neighborhood,
            address_detail,
            self._zip_code
        )


class AddressFactory:
    _address: Dict = {}

    def _get_key(self, **kwargs):
        return ''.join(kwargs.values())

    def get_address(self, **kwargs):
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._address[key]
            print("Usando objeto já criado")
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._address[key] = address_flyweight
            print("Criando novo objeto")

        return address_flyweight


if __name__ == "__main__":
    address_factory = AddressFactory()
    a1 = address_factory.get_address(
        street="Rua X",
        neighborhood="25° District",
        zip_code="04002-8922"
    )

    a2 = address_factory.get_address(
        street="Rua X",
        neighborhood="25° District",
        zip_code="04002-8922"
    )

    joao = Client("João")
    joao.address_number = "50"
    joao.address_details = "Block X - 12°"
    joao.add_address(a1)
    joao.list_addresses()

    joana = Client("Joana")
    joana.address_number = "50"
    joana.address_details = "Block Y - 1°"
    joana.add_address(a1)
    joana.list_addresses()

    print(a1 == a2)
