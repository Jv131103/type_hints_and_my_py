"""
GoF - Memento é um padrão de projeto comportamental
que tem a intenção de permitir que você salve e restaure
um estado anterior de um objeto originator sem revelar os
detalhes da sua implementação e sem violar o encapsulamento.

Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usado para armazenar mementos.
Caretaker também é usado com o Padrão Command.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List


class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__("_state", state)

    def get_state(self) -> Dict:
        return self._state

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError("Sorry, I am immutable")


class ImageEditor:
    def __init__(
            self,
            name: str,
            width: int,
            height: int,
            image_code_generator_bloob: str
    ) -> None:
        self.name = name
        self.width = width
        self.height = height
        self.image_code_generator_bloob = image_code_generator_bloob

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"


class Caretaker:
    def __init__(self, orginator: ImageEditor) -> None:
        self._orginator = orginator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._orginator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return
        self._orginator.restore(self._mementos.pop())


if __name__ == "__main__":
    img = ImageEditor(
        "FOTO_1.jpg",
        500,
        500,
        "FFD8FFE000104A4649460001010100..."
    )
    print(img)
    caretaker = Caretaker(img)
    caretaker.backup()

    img.name = "FOTO_2.jpg"
    img.image_code_generator_bloob = '89504E470D0A1A0A0000000D494844...'
    caretaker.backup()

    img.name = "FOTO_3.jpg"
    img.image_code_generator_bloob = '99504E470D0A1B0V0000000D4948976...'
    caretaker.backup()

    img.name = "FOTO_4.jpg"
    img.image_code_generator_bloob = '15004E470D0A1B0V0000000D1234567...'

    caretaker.restore()

    print(img)

    caretaker.restore()

    print(img)

    caretaker.restore()

    print(img)

    caretaker.restore()

    print(img)
