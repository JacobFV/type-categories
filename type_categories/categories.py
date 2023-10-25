from typing import (
    Any,
    Union,
    Optional,
    TypeVar,
    Generic,
    Type,
    Callable,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    Sequence,
    MutableSequence,
    Set,
    MutableSet,
    ByteString,
    MutableSequence,
)
from types import (
    ModuleType,
    FunctionType,
    MethodType,
    GeneratorType,
    AsyncGeneratorType,
)

atomic_types = bool | int | float | complex | str | bytes | bytearray

container_types = Mapping | Sequence | Iterator | GeneratorType | AsyncGeneratorType

callable_types = FunctionType | MethodType | Callable

meta_types = Generic | TypeVar

composite_types = container_types | ModuleType | object


__all__ = [
    "atomic_types",
    "container_types",
    "callable_types",
    "meta_types",
    "composite_types",
]
