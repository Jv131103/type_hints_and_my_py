from typing import Protocol, runtime_checkable

# ============= ABSTRAÇÕES (interfaces) =============


@runtime_checkable
class CozinharBatata(Protocol):
    def cozinhar(self) -> str: ...


@runtime_checkable
class Servir(Protocol):
    def servir(self, prato: str) -> str: ...


@runtime_checkable
class Molho(Protocol):
    def servir_molho(self) -> str: ...


# ============= IMPLEMENTAÇÕES PEQUENAS (SRP) =============

class Fritadeira:  # S: só cozinha
    def cozinhar(self) -> str:
        return "Batata frita"


class Forno:  # S: só cozinha (outra forma)
    def cozinhar(self) -> str:
        return "Batata assada"


class Garcom:  # S: só serve
    def servir(self, prato: str) -> str:
        return f"Servindo: {prato}"


class Ketchup:  # S: só o molho
    def servir_molho(self) -> str:
        return "Ketchup"


class Maionese:
    def servir_molho(self) -> str:
        return "Maionese"


# ============= ALTO NÍVEL DEPENDENDO DE ABSTRAÇÕES (DIP) =============

class Restaurante:
    """
    D: depende de abstrações (CozinharBatata, Servir, Molho),
       e não de classes concretas.
    """
    def __init__(self, cozinha: CozinharBatata, garcom: Servir, molho: Molho):
        self._cozinha = cozinha
        self._garcom = garcom
        self._molho = molho

    def pedido(self) -> str:
        prato = self._cozinha.cozinhar()
        servido = self._garcom.servir(prato)
        return f"{servido} com {self._molho.servir_molho()}"


# ============= USO (OCP, LSP, ISP em ação) =============

if __name__ == "__main__":
    # OCP: trocar a estratégia sem modificar Restaurante
    r1 = Restaurante(cozinha=Fritadeira(), garcom=Garcom(), molho=Ketchup())
    print(r1.pedido())  # Servindo: Batata frita com Ketchup

    r2 = Restaurante(cozinha=Forno(), garcom=Garcom(), molho=Maionese())
    print(r2.pedido())  # Servindo: Batata assada com Maionese

    # LSP: qualquer classe que implemente o "contrato" pode substituir a outra
    class Barbecue(Molho):
        def servir_molho(self) -> str:
            return "Barbecue"

    r3 = Restaurante(cozinha=Fritadeira(), garcom=Garcom(), molho=Barbecue())
    print(r3.pedido())  # Servindo: Batata frita com Barbecue

    # ISP: interfaces pequenas e específicas (cozinhar/servir/molho separados)
    # Se criarmos um Robô que só cozinha, ele não é obrigado a "servir"
    class RoboCozinheiro:
        def cozinhar(self) -> str:
            return "Batata na pressão"

    r4 = Restaurante(
        cozinha=RoboCozinheiro(),
        garcom=Garcom(),
        molho=Ketchup()
    )
    print(r4.pedido())  # Servindo: Batata na pressão com Ketchup
