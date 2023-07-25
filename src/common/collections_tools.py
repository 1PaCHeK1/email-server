from collections.abc import Iterable, Sequence

from typing import TypeVar


T = TypeVar("T")

def batched(data: Sequence[T], size: int = 5) -> Iterable[Sequence[T]]:
    start = 0
    for _ in range(0, len(data), size):
        yield data[start: start+size]
        start += size
