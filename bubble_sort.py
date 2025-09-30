"""Simple implementation of bubble sort."""
from typing import MutableSequence, TypeVar

T = TypeVar("T")

def bubble_sort(values: MutableSequence[T]) -> MutableSequence[T]:
    """Sort ``values`` in-place using the bubble sort algorithm.

    Args:
        values: A mutable sequence of comparable items.

    Returns:
        The same sequence instance, sorted in non-decreasing order.
    """
    n = len(values)
    if n < 2:
        return values

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:
            break
    return values


def _demo() -> None:
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Before:", numbers)
    bubble_sort(numbers)
    print("After: ", numbers)


if __name__ == "__main__":
    _demo()
