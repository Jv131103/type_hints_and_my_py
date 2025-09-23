"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory é que
o Factory Method usa herança, enquanto Abstract Factory usa composição.

Princípio: programe para interfaces, não para implementações
"""

from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN está buscando o cliente...')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZN está buscando o cliente...')


class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto ZN está buscando o cliente...')


class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZN está buscando o cliente...')


class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZS está buscando o cliente...')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZS está buscando o cliente...')


class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto ZS está buscando o cliente...')


class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZS está buscando o cliente...')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo(tipo: str) -> VeiculoLuxo:
        pass

    @staticmethod
    @abstractmethod
    def get_carro_popular(tipo: str) -> VeiculoPopular:
        pass

    @staticmethod
    @abstractmethod
    def get_moto_luxo(tipo: str) -> VeiculoLuxo:
        pass

    @staticmethod
    @abstractmethod
    def get_moto_popular(tipo: str) -> VeiculoPopular:
        pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:  # type: ignore
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:  # type: ignore
        return CarroPopularZN()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:  # type: ignore
        return MotoLuxoZN()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:  # type: ignore
        return MotoPopularZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:  # type: ignore
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:  # type: ignore
        return CarroPopularZS()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:  # type: ignore
        return MotoLuxoZS()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:  # type: ignore
        return MotoPopularZS()


class Cliente:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()


if __name__ == "__main__":
    cliente = Cliente()
    cliente.busca_clientes()
