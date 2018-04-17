import pytest

from ml.search import binary_search, linear_search


@pytest.mark.parametrize('algorithm', [binary_search, linear_search])
@pytest.mark.parametrize('input_,v,expected', [
    ([2, 3, 5, 7], 2, 0),
    ([2, 3, 5, 7], 5, 2),
    ([2, 3, 5, 7], 9, -1)
])
def test_search(algorithm, input_, v, expected):
    assert algorithm(input_, v) == expected
