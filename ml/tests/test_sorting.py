import pytest

from ml.sorting import (
    bubble_sort,
    insertion_sort,
    selection_sort
)


@pytest.mark.parametrize('algorithm',
    [bubble_sort, insertion_sort, selection_sort])
@pytest.mark.parametrize('original,expected', [
    ([1, 5, 2, 1], [1, 1, 2, 5]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([10, -1, 0], [-1, 0, 10]),
    ([-1, -50, -100], [-100, -50, -1]),
    ([0], [0])
])
def test_bubble(algorithm, original, expected):
    assert algorithm(original) == expected
