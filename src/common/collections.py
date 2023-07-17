from collections.abc import Iterable

from typing import TypeVar


T = TypeVar("T")

def batched(data: Iterable[T], size: int = 5) -> Iterable[T]:
    start = 0
    for _ in range(0, len(data), size):
        yield data[start: start+size]
        start += size
