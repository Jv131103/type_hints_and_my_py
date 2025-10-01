from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str:
        pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['A', 'B', 'C']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f"HandlerABC: conseguiu tartar o valor {letter}"
        return self.sucessor.handle(letter)


class HandleDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['D', 'E', 'F']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f"HandlerDEF: conseguiu tartar o valor {letter}"
        return self.sucessor.handle(letter)


class HandleFallback(Handler):
    def handle(self, letter: str) -> str:
        return f"handlers não encotraram {letter}"


if __name__ == "__main__":
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    handler_unsolved = HandleFallback()
    handler_def = HandleDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)

    for letra in letras:
        print(handler_abc.handle(letra.upper()))
