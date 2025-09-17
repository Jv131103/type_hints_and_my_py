"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:

    . Permite criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    . Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory)

    . Podem facilitar o processo de "cache" ou criação de "singletons" porque
    a fábrica pode retornar um objeto já criado para o cliente, ao invés de
    criar novos objetos sempre que o cliente precisar.

Desvantagens:

    . Podem introduzir muitas classes no código


Vamos ver 2 tipos de Factory da GoF: Factory Method e Abstract Factory

Aqui:

    Simple Factory <- Uma espécie de Factory Method parametrizado
    Simple Factory pode não ser considerado um padrão de projeto por si só
    Simple Factory pode quebrar os princípios de SOLID
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo buscando cliente...")


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular buscando cliente...")


class MotoTaxi(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto taxi buscando cliente...")


class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        match tipo.lower():
            case "luxo":
                return CarroLuxo()
            case "popular":
                return CarroPopular()
            case "moto_taxi":
                return MotoTaxi()
            case _:
                assert 0, f"O veículo {tipo} não existe!"


if __name__ == "__main__":
    import random

    carros_disponiveis = ["luxo", "popular", "moto_taxi"]
    for i in range(10):
        carro = VeiculoFactory().get_carro(random.choice(carros_disponiveis))
        carro.buscar_cliente()
