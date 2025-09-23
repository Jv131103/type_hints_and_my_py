"""
O singleton tem a intenção de gerantir que uma classe tenha somente uma
instância e fornece um ponto global de acesso para a mesma.
"""


class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


if __name__ == "__main__":
    as1 = AppSettings()
    as2 = AppSettings()

    print(as1)
    print(as2)
    print(as1 == as2)
    print(id(as1) == id(as2))

    as1.nome = "Joao"  # type: ignore
    print(as2.nome)    # type: ignore
