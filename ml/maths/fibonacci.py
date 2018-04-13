def fibonacci(n, _start=0, _accumulator=None):
    """Compute the first *n* Fibonacci numbers.

    Args:
        _start [int]: Optional starting point. Default is 0. The end user
        should not use this argument.
        n [int]: number of numbers to return in the list.
        _accumulator [list]: Optional argument to pass in the recursive call
        the current list of Fibonacci numbers up to that iteration. The end
        user should not use this argument.
    Returns:
        A [list] with the first *n* numbers in the Fibonacci series.
    """
    if not _accumulator:
        _accumulator = []
    while n > 0:
        if _start == 0 or len(_accumulator) == 0:
            return fibonacci(_start=_start+1, n=n-1, _accumulator=[_start])
        else:
            _start, _accumulator = _start + _accumulator[-1], _accumulator + [_start]
            return fibonacci(_start=_start, n=n-1, _accumulator=_accumulator)
    return _accumulator


def fibonacci_to(n):
    """Fibonacci function.

    Args:
        n [int]: The index of the number on the Fibonacci series to return.
    Returns:
        The *n* number [int] in the Fibonacci series.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_between(start, end):
    """Compute all numbers in the Fibonacci series between *start* and *end*.

    Args:
        start [int]: The minimum number in the series.
        end [int]: The maximum number in the series.
    Returns:
        A [list] of numbers in the Fibonacci series between *start* and *end*.
        *start* and *end* will be included in the list only if they are
        themselves Fibonacci numbers.
    """
    full_series = fibonacci(n=end)
    return [n for n in full_series if end >= n >= start]
