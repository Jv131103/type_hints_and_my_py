# -*- coding: utf-8 -*-
"""
tipos_geradores_guide.py
========================
Guia prático e comentado de type hints modernos em Python (3.11+),
incluindo:
- Primitivos, coleções, dicionários, sets
- Unions, Optional, Literal, Final, ClassVar
- Type aliases (TypeAlias), NewType
- TypedDict (Required/NotRequired)
- Annotated (metadados/validação)
- Protocol (duck typing) e @runtime_checkable
- TypeVar/Bound, variância, Generic
- Callable, ParamSpec, Concatenate, overload
- cast, assert_never, NoReturn
- Iterables x Iterators x Generators (sync/async)
- Context managers e coleções ABC modernas
- Boas práticas e armadilhas

Compat: Python 3.11+. Para 3.8–3.10 use typing_extensions quando indicado.
Docs: https://docs.python.org/3/library/typing.html
"""
from __future__ import annotations

# Context managers:
from contextlib import asynccontextmanager, contextmanager
# ---------------------------------------------------------------------
# Imports de typing (com fallback para versões antigas)
# ---------------------------------------------------------------------
from typing import (TYPE_CHECKING, Annotated, Any, AsyncContextManager,
                    AsyncGenerator, AsyncIterable, AsyncIterator, Callable,
                    ClassVar, Concatenate, ContextManager, Deque, Dict, Final,
                    FrozenSet, Generator, Generic, Iterable, Iterator, List,
                    Literal, Mapping, MutableMapping, NoReturn, Optional,
                    ParamSpec, Protocol, Self, Sequence, Set, Tuple, TypedDict,
                    TypeVar, Union, assert_never, cast, overload,
                    runtime_checkable)

try:
    # Para 3.11+ já existem, mas mantemos fallback ilustrativo
    from typing import LiteralString, NotRequired, Required, TypeAlias
except Exception:  # pragma: no cover - fallback para 3.8–3.10
    from typing_extensions import (LiteralString, NotRequired,  # type: ignore
                                   Required, TypeAlias)

from typing import NewType

# ---------------------------------------------------------------------
# 0) Primitivos e noções básicas
# ---------------------------------------------------------------------
numeros: int = 10
flutuante: float = 10.5
complexo: complex = 12j
booleano: bool = True
string: str = "Olá"

# Observação: Use tipos embutidos parametrizados
# (Python 3.9+): list[int], dict[str, int] etc.

# preferível a List[int] (que segue válido)
lista_simples: list[int] = [1, 2, 3, 4]

# ---------------------------------------------------------------------
# 1) Sequências e Tuplas
# - list é invariável; Sequence é covariante (apenas leitura)
# ---------------------------------------------------------------------
lista2: List[str] = ["teste"]  # forma antiga, ainda aceita
lista_mista: list[int | str] = [123, "JOAO"]
lista_mista2: list[Union[int, float, str, bool]] = [True, 0, "X", 3.14159]

# Tuplas: tamanho e tipos podem ser fixados
tupla_livre: tuple = (0, 1, 2, 3)
tupla_fix: Tuple[int, int, int, int] = (1, 2, 3, 4)
tupla_heterogenea: tuple[int, str, bool] = (7, "x", False)
tupla_variadica: tuple[int, ...] = (1, 2, 3, 4, 5)

# ---------------------------------------------------------------------
# 2) Dicionários, Sets e Mapeamentos
# ---------------------------------------------------------------------
dicionario_simples: dict[str, str] = {"chave": "valor"}

# Mapping (apenas leitura) vs MutableMapping (leitura+escrita)
mapa_ro: Mapping[str, list[int]] = {"key": [1, 2, 3, 4]}
mapa_rw: MutableMapping[str, list[int]] = {"key": [1, 2, 3, 4]}

dicionario_misto: Dict[str, Union[list[int], str, int]] = {
    "key": [1, 2, 3, 4],
    "key2": "076a9c7be65beab332f14a0b8d9b5c6d",
    "key3": 42,
}

# Any significa “qualquer coisa”; evite em APIs públicas sem necessidade
dicionario_any: dict[str, Any] = {"user": "x", "pass": 1234567}

# Alias de tipo (2 formas)
MeuTipo = Dict[str, Union[str, int, list[int]]]
meu_tipo: TypeAlias = dict[str, str | int | list[int]]

dicionario5: MeuTipo = {"key1": [1, 2, 3, 4], "key2": "passwd"}

# Sets
conjunto: set[int] = {1, 2, 3, 4, 5, 6}
conjunto_imutavel: FrozenSet[str] = frozenset({"a", "b"})

# ---------------------------------------------------------------------
# 3) NewType e TypeAlias
# ---------------------------------------------------------------------
UserID = NewType("UserID", int)
# ajuda validadores/mypy a não confundir com int cru
user_id: UserID = UserID(3243434312)


# ---------------------------------------------------------------------
# 4) Literal, LiteralString, Final, ClassVar
# ---------------------------------------------------------------------
ModoIO = Literal["r", "w", "a", "rb", "wb"]


def abrir_caminho(path: str, modo: ModoIO = "r") -> None:
    # Em tempo de execução é só str, mas ferramentas estáticas
    # restringem valores
    pass


# LiteralString (segurança: evitar format strings de origem não confiável)
def usa_sql(query: LiteralString) -> None:
    pass


# Constantes
PI: Final[float] = 3.141592653589793


class Config:
    DEFAULT_TIMEOUT: ClassVar[int] = 30  # atributo de classe, não de instância

    def __init__(self, host: str) -> None:
        self.host: str = host


# ---------------------------------------------------------------------
# 5) Optional/Union e boas práticas
# - Optional[T] == T | None
# - Prefira “T | None” (Python 3.10+)
# ---------------------------------------------------------------------
def busca_usuario(nome: str) -> str | None:
    return nome if nome else None


def usa_usuario() -> None:
    u = busca_usuario("joao")
    if u is not None:
        print(u.upper())  # narrow por checagem de None


# ---------------------------------------------------------------------
# 6) TypedDict (estruturas “tipo dict” tipadas, úteis para dados JSON)
# - Required/NotRequired controlam obrigatoriedade por chave
# ---------------------------------------------------------------------
class Credenciais(TypedDict, total=False):
    user: Required[str]
    password: Required[str]
    otp: NotRequired[str]
    remember_me: NotRequired[bool]


def autenticar(cfg: Credenciais) -> bool:
    # Ferramentas estáticas alertam se faltar 'user'/'password'
    return True


# ---------------------------------------------------------------------
# 7) Annotated: metadados para validação/documentação
# ---------------------------------------------------------------------
def _range_0_100(x: int) -> int:
    if not (0 <= x <= 100):
        raise ValueError("fora de [0,100]")
    return x


Score = Annotated[int, "0..100", _range_0_100]


def registra_score(s: Score) -> None:
    # Em runtime, você pode aplicar validadores se quiser
    # (frameworks fazem isso)
    pass


# ---------------------------------------------------------------------
# 8) Protocol e duck typing (estrutural)
# - Útil para definir “contratos” independentes de herança nominal
# ---------------------------------------------------------------------
@runtime_checkable
class TemLen(Protocol):
    def __len__(self) -> int: ...


def tamanho(x: TemLen) -> int:
    return len(x)


assert isinstance("abc", TemLen)  # True por protocolo estrutural


# Protocol com atributos e métodos
class Arquivavel(Protocol):
    caminho: str
    def salvar(self) -> None: ...


class Documento:
    caminho: str

    def __init__(self, caminho: str) -> None:
        self.caminho = caminho

    def salvar(self) -> None:
        print(f"Salvando em {self.caminho}")


def persistir(item: Arquivavel) -> None:
    item.salvar()


# ---------------------------------------------------------------------
# 9) TypeVar, Generic e variância
# - list[T] é INVARIANTE
# - Sequence[T] é COVARIANTE (leitura)
# - Callable[[Super], Sub] é CONTRAVARIANTE no argumento, COVARIANTE no retorno
# ---------------------------------------------------------------------
T = TypeVar("T")
NumberT = TypeVar("NumberT", int, float)  # bound por conjunto discreto


class Caixa(Generic[T]):
    def __init__(self, valor: T) -> None:
        self.valor = valor

    def get(self) -> T:
        return self.valor


def primeiro(seq: Sequence[T]) -> T:
    return seq[0]


# Bound por protocolo (ex.: comparável)
class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


C = TypeVar("C", bound=Comparable)


def minimo(a: C, b: C) -> C:
    return a if a < b else b


# ---------------------------------------------------------------------
# 10) Callable, ParamSpec, Concatenate, overload
# ---------------------------------------------------------------------
P = ParamSpec("P")
R = TypeVar("R")


def logger(fn: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"[LOG] call {fn.__name__} args={args} kwargs={kwargs}")
        return fn(*args, **kwargs)
    return wrapper


# Concatenate permite “amarrar” self/ctx no tipo do wrapper de métodos
S = TypeVar("S")


def com_ctx(
        fn: Callable[Concatenate[S, P], R]
) -> Callable[Concatenate[S, P], R]:
    return fn


# overload: perfis de chamada distintos e tipos de retorno diferentes
@overload
def carrega(path: str) -> bytes: ...


@overload
def carrega(path: str, *, texto: Literal[True]) -> str: ...


def carrega(path: str, *, texto: bool = False) -> bytes | str:
    with open(path, "rb") as f:
        data = f.read()
    return data.decode("utf-8") if texto else data


# ---------------------------------------------------------------------
# 11) cast, assert_never, NoReturn, narrowing e pattern matching
# ---------------------------------------------------------------------
def so_str(x: Any) -> str:
    if not isinstance(x, str):
        # Apenas para satisfazer tipo estático; não muda runtime
        x = cast(str, str(x))
    return x


Cor = Literal["red", "green", "blue"]


def pinta(cor: Cor) -> None:
    if cor == "red":
        pass
    elif cor == "green":
        pass
    elif cor == "blue":
        pass
    else:
        assert_never(cor)  # garante exaustividade


def aborta(msg: str) -> NoReturn:
    raise RuntimeError(msg)


# Python pattern matching também realiza narrowing
def processa(evento: dict[str, Any]) -> None:
    match evento.get("tipo"):
        case "login":
            usuario = evento.get("user")
            if isinstance(usuario, str):
                print(usuario.upper())
        case "logout":
            pass
        case outro:
            print("ignorado:", outro)


# ---------------------------------------------------------------------
# 12) Iterables, Iterators e Generators (sync/async)
# ---------------------------------------------------------------------
# Iterable[T]: produz um Iterator[T] (p.ex. objetos usados em for-in)
# Iterator[T]: tem __next__() -> T e __iter__() -> self
# Generator[Y, SendT, ReturnT]: yield Y, recebe com send() tipo SendT, retorna
# ReturnT no StopIteration
def duplica_sequencia(seq: Sequence[int]) -> list[int]:
    return [x * 2 for x in seq]


def multiplica_iteravel(seq: Iterable[int], k: int) -> list[int]:
    return [x * k for x in seq]


# Função geradora (Generator[int, None, None])
def contagem(n: int) -> Generator[int, None, None]:
    i = 0
    while i < n:
        yield i
        i += 1


# yield from delega para outro iterável/gerador
def flat(
        lista_de_listas: Iterable[Iterable[int]]
) -> Generator[int, None, None]:
    for sub in lista_de_listas:
        yield from sub


# Gerador que aceita send()
def eco() -> Generator[str, str, str]:
    """
    Y (yield) = str emitido,
    SendT = str recebido via .send(),
    ReturnT = str retornado no StopIteration
    """
    recebido = yield "start"
    while recebido != "stop":
        recebido = yield f"eco: {recebido}"
    return "bye"


# Async generator
async def gen_async(n: int) -> AsyncGenerator[int, None]:
    for i in range(n):
        yield i  # consumir com: async for x in gen_async(...)

# Diferença de tipos:
iteravel_str: Iterable[str] = ["a", "b"]
iterador_str: Iterator[str] = iter(iteravel_str)
gerador_int: Generator[int, None, None] = contagem(3)

# Async tipos:
async_iteravel: AsyncIterable[int]
async_iterador: AsyncIterator[int]


@contextmanager
def recurso() -> Iterator[str]:
    yield "ok"  # T = str


@asynccontextmanager
async def recurso_async() -> AsyncIterator[str]:
    yield "ok"  # T = str


# ---------------------------------------------------------------------
# 13) Classes com tipos, Self e métodos fluentes
# ---------------------------------------------------------------------
class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> Self:
        print(f"{self.nome} está falando")
        return self

    def aniversaria(self) -> Self:
        self.idade += 1
        return self  # método fluente com Self


# ---------------------------------------------------------------------
# 14) Exemplo de uso + pequenas demonstrações
# ---------------------------------------------------------------------
def _demo_basico() -> None:
    p1 = Pessoa("João", "Justino", 21)
    p1.fala().aniversaria().fala()  # encadeável por Self

    print(duplica_sequencia(range(0, 6)))
    print(multiplica_iteravel(range(0, 6), 3))

    g = contagem(3)
    print(list(g))  # [0,1,2]

    # Exemplo send()/return
    e = eco()
    print(next(e))              # "start"
    print(e.send("oi"))         # "eco: oi"
    print(e.send("tudo bem"))   # "eco: tudo bem"
    try:
        e.send("stop")          # StopIteration: value "bye"
    except StopIteration as ex:
        print("retorno do gerador:", ex.value)

    # TypedDict
    autenticar({"user": "x", "password": "y", "remember_me": True})

# ---------------------------------------------------------------------
# 15) Pitfalls e boas práticas (comentários rápidos)
# - Evite Any desnecessário; prefira tipos mais precisos ou Protocols.
# - Não use list para parâmetros quando leitura apenas: prefira Sequence[T].
# - Não materialize geradores com list(...) sem necessidade.
# - Em APIs públicas, evite Optional “escondido”: deixe claro T | None.
# - Em overloads, mantenha implementação compatível com os stubs @overload.
# - Para dados JSON estáveis, prefira TypedDict/Protocol a dict[str, Any].
# ---------------------------------------------------------------------


if __name__ == "__main__":
    _demo_basico()

"""
Referências rápidas:
- typing — https://docs.python.org/3/library/typing.html
- collections.abc (Iterável/Iterador/Generator/Async…) — preferir em checagens
- typing_extensions — backports úteis (3.8–3.10)
Ferramentas:
- mypy:    mypy tipos_geradores_guide.py --strict
- pyright: pyright tipos_geradores_guide.py
"""
