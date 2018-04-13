import pytest

from maths.fibonacci import fibonacci, fibonacci_between, fibonacci_to


@pytest.mark.parametrize('n,expected', [
    (0, []),
    (1, [0]),
    (2, [0, 1]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
])
def test_fibonacci_series_no_start(n, expected):
    assert fibonacci(n=n) == expected


@pytest.mark.parametrize('test_input,expected', [
    (0, 0),
    (1, 1),
    (13, 233),
    (100, 354224848179261915075)
])
def test_fibonacci_up_to_n(test_input, expected):
    assert fibonacci_to(test_input) == expected


@pytest.mark.parametrize('start,end,expected', [
    (2, 200, [2, 3, 5, 8, 13, 21, 34, 55, 89, 144]),
    (6, 200, [8, 13, 21, 34, 55, 89, 144]),
    (5, 150, [5, 8, 13, 21, 34, 55, 89, 144])
])
def test_fibonacci_between(start, end, expected):
    assert fibonacci_between(start, end) == expected
