# -*- coding: utf-8 -*-
"""
arquivo_completo_typing.py
==========================
Exemplo completo, PEP 8 e tipado (Python 3.11+), cobrindo:

- Primitivos e coleções (list/tuple/dict/set) com tipos embutidos
- Unions, Optional, Literal, Final, ClassVar
- Type aliases (TypeAlias), NewType
- TypedDict (Required/NotRequired)
- Annotated (metadados/validação simples)
- Protocol (duck typing) e @runtime_checkable
- TypeVar/Generic/variância; Callable, ParamSpec, Concatenate, overload
- cast, assert_never, NoReturn; narrowing com pattern matching
- Iterables × Iterators × Generators (sync/async) e context managers
- Classe com métodos fluentes usando Self
- Função main de demonstração sob o guard padrão

Compatível com mypy/pyright. Para 3.8–3.10 use typing_extensions onde indicado.
Documentação oficial: https://docs.python.org/3/library/typing.html
"""

from __future__ import annotations

# Prefira collections.abc para ABCs de containers/iteradores/geradores.
from collections.abc import (AsyncGenerator, AsyncIterable, AsyncIterator,
                             Callable, Generator, Iterable, Iterator, Mapping,
                             MutableMapping, Sequence)
from contextlib import asynccontextmanager, contextmanager
from dataclasses import dataclass
from typing import (TYPE_CHECKING, Annotated, Any, ClassVar, Concatenate,
                    Final, Literal, LiteralString, NewType, NoReturn, Optional,
                    ParamSpec, Protocol, Self, TypeAlias, TypedDict, TypeVar,
                    assert_never, cast, overload, runtime_checkable)

# -----------------------------------------------------------------------------
# 0) Primitivos e coleções
# -----------------------------------------------------------------------------

NUM_MAX_ITENS: Final[int] = 10

inteiro: int = 42
flutuante: float = 3.14
comp: complex = 2 + 3j
booleano: bool = True
texto: str = "Olá, mundo!"

lista: list[int] = [1, 2, 3]
tupla_fix: tuple[int, int, int] = (1, 2, 3)
tupla_var: tuple[int, ...] = (1, 2, 3, 4, 5)

dicionario: dict[str, int] = {"a": 1, "b": 2}
conjunto: set[str] = {"x", "y"}

# Mapeamentos (somente leitura/leitura+escrita)
map_ro: Mapping[str, list[int]] = {"k": [1, 2, 3]}
map_rw: MutableMapping[str, list[int]] = {"k": [1, 2, 3]}

# -----------------------------------------------------------------------------
# 1) TypeAlias, NewType, Literal, Optional
# -----------------------------------------------------------------------------

HexStr: TypeAlias = str
UserID = NewType("UserID", int)


def busca_usuario(nome: str) -> str | None:
    """Retorna o nome do usuário ou None se não encontrado."""
    return nome or None


ModoIO = Literal["r", "w", "a", "rb", "wb"]


def abrir_caminho(_caminho: str, modo: ModoIO = "r") -> None:
    """Exemplo de parâmetro restrito por Literal (checado estaticamente)."""
    _ = modo  # apenas para suprimir linters
    return None


# -----------------------------------------------------------------------------
# 2) TypedDict, Required/NotRequired, Annotated
# -----------------------------------------------------------------------------

try:
    from typing import NotRequired, Required
except Exception:  # pragma: no cover
    from typing_extensions import NotRequired, Required  # type: ignore


class Credenciais(TypedDict, total=False):
    user: Required[str]
    password: Required[str]
    otp: NotRequired[str]
    remember_me: NotRequired[bool]


def autenticar(cfg: Credenciais) -> bool:
    """Exemplo simples; checadores estáticos exigirão user/password."""
    return bool(cfg.get("user") and cfg.get("password"))


def _range_0_100(x: int) -> int:
    if not (0 <= x <= 100):
        raise ValueError("fora de [0, 100]")
    return x


Score = Annotated[int, "0..100", _range_0_100]


def registrar_score(score: Score) -> None:
    """Recebe um score anotado com metadados de validação."""
    _ = score


# -----------------------------------------------------------------------------
# 3) Protocol / duck typing
# -----------------------------------------------------------------------------

@runtime_checkable
class TemLen(Protocol):
    def __len__(self) -> int: ...


def tamanho(x: TemLen) -> int:
    return len(x)


class Arquivavel(Protocol):
    caminho: str
    def salvar(self) -> None: ...


@dataclass(slots=True)
class Documento:
    caminho: str

    def salvar(self) -> None:
        print(f"Salvando em {self.caminho}")


def persistir(item: Arquivavel) -> None:
    item.salvar()


# -----------------------------------------------------------------------------
# 4) Generics, TypeVar e utilidades
# -----------------------------------------------------------------------------

T = TypeVar("T")
U = TypeVar("U")
R = TypeVar("R")
P = ParamSpec("P")
S_ = TypeVar("S_")


def primeiro(seq: Sequence[T]) -> T:
    return seq[0]


class Caixa(Sequence[T]):
    """Sequência imutável minimalista, apenas para exemplificar Generic."""

    __slots__ = ("_dados",)

    def __init__(self, dados: Sequence[T]) -> None:
        self._dados: tuple[T, ...] = tuple(dados)

    def __len__(self) -> int:  # Sequence
        return len(self._dados)

    def __getitem__(self, i: int) -> T:  # Sequence
        return self._dados[i]


def mapear(func: Callable[[T], U], itens: Iterable[T]) -> list[U]:
    return [func(x) for x in itens]


# -----------------------------------------------------------------------------
# 5) Callable, overload, ParamSpec, Concatenate
# -----------------------------------------------------------------------------

def logger(fn: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"[LOG] {fn.__name__} args={args} kwargs={kwargs}")
        return fn(*args, **kwargs)
    return wrapper


def com_ctx(
        fn: Callable[Concatenate[S_, P], R]
) -> Callable[Concatenate[S_, P], R]:
    return fn


@overload
def carregar(path: str) -> bytes: ...
@overload
def carregar(path: str, *, texto: Literal[True]) -> str: ...


def carregar(path: str, *, texto: bool = False) -> bytes | str:
    with open(path, "rb") as f:
        data = f.read()
    return data.decode("utf-8") if texto else data


# -----------------------------------------------------------------------------
# 6) cast, assert_never, NoReturn, narrowing
# -----------------------------------------------------------------------------

Cor = Literal["red", "green", "blue"]


def pinta(cor: Cor) -> None:
    if cor == "red":
        pass
    elif cor == "green":
        pass
    elif cor == "blue":
        pass
    else:
        assert_never(cor)


def aborta(msg: str) -> NoReturn:
    raise RuntimeError(msg)


def so_str(x: Any) -> str:
    """Exemplo de cast: útil para satisfazer o checador estático."""
    if not isinstance(x, str):
        x = cast(str, str(x))
    return x


def processa_evento(evento: dict[str, Any]) -> None:
    match evento.get("tipo"):
        case "login":
            user = evento.get("user")
            if isinstance(user, str):
                print(user.upper())
        case "logout":
            pass
        case other:
            print("ignorado:", other)


# -----------------------------------------------------------------------------
# 7) Iterables × Iterators × Generators (sync/async) e context managers
# -----------------------------------------------------------------------------

def duplica(seq: Sequence[int]) -> list[int]:
    return [x * 2 for x in seq]


def multiplica(seq: Iterable[int], k: int) -> list[int]:
    return [x * k for x in seq]


def contagem(n: int) -> Generator[int, None, None]:
    i = 0
    while i < n:
        yield i
        i += 1


def flat(nested: Iterable[Iterable[T]]) -> Generator[T, None, None]:
    for sub in nested:
        yield from sub


def eco() -> Generator[str, str, str]:
    """Yield inicial, recebe via .send, e retorna 'bye' no StopIteration."""
    recebido = yield "start"
    while recebido != "stop":
        recebido = yield f"eco: {recebido}"
    return "bye"


async def gen_async(n: int) -> AsyncGenerator[int, None]:
    for i in range(n):
        yield i


@contextmanager
def recurso() -> Iterator[str]:
    # Nota: anote a função como Iterator[T] (geradora); o decorador
    # a transformará em ContextManager[T] no uso.
    yield "ok"


@asynccontextmanager
async def recurso_async() -> AsyncIterator[str]:
    yield "ok"


# -----------------------------------------------------------------------------
# 8) Classe fluente com Self
# -----------------------------------------------------------------------------

@dataclass(slots=True)
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    def fala(self) -> Self:
        print(f"{self.nome} está falando")
        return self

    def aniversaria(self) -> Self:
        self.idade += 1
        return self


# -----------------------------------------------------------------------------
# 9) Demonstração segura (sem encadeamentos inválidos)
# -----------------------------------------------------------------------------

@logger
def soma(a: int, b: int) -> int:
    return a + b


def _demo() -> None:
    # Optional/Union
    u = busca_usuario("joao")
    if u is not None:
        print(u.upper())

    # Protocol e persistência
    doc = Documento("/tmp/arquivo.txt")
    persistir(doc)

    # Generic e Sequence
    cx = Caixa([10, 20, 30])
    print(primeiro(cx))

    # Mapear
    print(mapear(lambda z: z * 10, [1, 2, 3]))

    # Overload
    _ = carregar(__file__)           # bytes
    _ = carregar(__file__, texto=True)  # str

    # Geradores
    print(list(contagem(3)))
    print(list(flat([[1, 2], [3]])))

    e = eco()
    print(next(e))             # "start"
    print(e.send("oi"))        # "eco: oi"
    print(e.send("tudo bem"))  # "eco: tudo bem"
    try:
        e.send("stop")
    except StopIteration as ex:
        print("retorno:", ex.value)  # "bye"

    # Context managers
    with recurso() as r:
        print("recurso:", r)

    # Classe fluente
    p = Pessoa("João", "Justino", 21)
    p.fala().aniversaria().fala()

    # Função decorada
    print("soma decorada:", soma(2, 3))


if __name__ == "__main__":
    _demo()
