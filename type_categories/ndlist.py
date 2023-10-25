from __future__ import annotations

from typing import Any, Generic, List, Type, TypeVar, Union

T = TypeVar("T")


class ndlist(Generic[T]):
    depth: int
    elem_type: Type[T]

    def __class_getitem__(cls, params):
        elem_type, depth = params
        return cls._get_nested_type(elem_type, depth)

    @classmethod
    def _get_nested_type(
        cls, elem_type: Type[T], depth: int
    ) -> Union[Type[T], List[Any]]:
        if depth == 0:
            return elem_type
        if depth == 1:
            return List[elem_type]
        return List[cls._get_nested_type(elem_type, depth - 1)]

    def depth(list: ndlist) -> int:
        depth = 0
        while isinstance(list, list):
            depth += 1
            list = list[0]
        return depth


__all__ = ["ndlist"]
