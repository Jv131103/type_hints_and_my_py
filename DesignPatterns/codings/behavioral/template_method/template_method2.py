from abc import ABC, abstractmethod


class Pizza(ABC):
    """Classe abstrata"""
    def prepare(self) -> None:
        """Template method"""
        self.hook_before_add_ingredients()
        self.add_ingredients()
        self.hook_after_add_ingredients()
        self.cook()
        self.cut()
        self.serve()

    @abstractmethod
    def add_ingredients(self) -> None:
        """Método abstrato"""
        pass

    @abstractmethod
    def cook(self) -> None:
        """Método abstrato"""
        pass

    def cut(self) -> None:
        """Método Concreto"""
        print(f"Contando a pizza {self.__class__.__name__}")

    def serve(self) -> None:
        """Método Concreto"""
        print(f"Servindo a pizza {self.__class__.__name__}")

    def hook_before_add_ingredients(self) -> None:
        '''Hook da classe'''
        pass

    def hook_after_add_ingredients(self) -> None:
        '''Hook da classe'''
        pass


class AModaCasa(Pizza):
    '''Subclasse da classe abstrata Pizza'''
    def add_ingredients(self) -> None:
        """Método abstrato"""
        print("AModaCasa: 2 queijos, Calabresa, molho, massa")

    def cook(self) -> None:
        """Método abstrato"""
        print("Preparando a pizza AModaCasa por 45 min no forno a lenha")


class Vegan(Pizza):
    '''Subclasse da classe abstrata Pizza'''
    def hook_before_add_ingredients(self) -> None:
        '''Hook usado antes da ação principal'''
        print('Vegan - Lavando ingredientes')

    def add_ingredients(self) -> None:
        print("Vegan: beringela, spinafre, salsa, massa, molho")

    def cook(self) -> None:
        print("Preparando a pizza Vegan por 10 min no forno a lenha")


if __name__ == "__main__":
    pedido_a_moda_da_casa = AModaCasa()
    pedido_a_moda_da_casa.prepare()
    print()
    pedido_vegan = Vegan()
    pedido_vegan.prepare()
