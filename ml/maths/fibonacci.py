


def fibonacci(n, start=0, accumulator=None):
    """Compute first n Fibonacci numbers.

    Args:
        start (int): Optional starting point. Default is 0. The end user
            should not use this argument.
        n (int): number of numbers to return in the list.
        accumulator (list): Optional argument to pass in the recursive call
            the current list of Fibonacci numbers up to that iteration. The end
            user should not use this argument.
    Returns:
        list: First n numbers in the Fibonacci series.
    """
    if not accumulator:
        accumulator = []
    while n > 0:
        if start == 0 or len(accumulator) == 0:
            return fibonacci(start=start+1, n=n-1, accumulator=[start])
        else:
            start, accumulator = start + accumulator[-1], accumulator + [start]
            return fibonacci(start=start, n=n-1, accumulator=accumulator)
    return accumulator


def fibonacci_to(n):
    """Fibonacci function.

    Args:
        n (int): The index of the number on the Fibonacci series to return.

    Returns:
        int: The n number in the Fibonacci series.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_between(start, end):
    """Compute all numbers in the Fibonacci series between *start* and *end*.

    Args:
        start (int): The minimum number in the series.
        end (int): The maximum number in the series.

    Returns:
        list: Numbers in the Fibonacci series between *start* and *end*.
            *start* and *end* will be included in the list only if they are
            themselves Fibonacci numbers.
    """
    full_series = fibonacci(n=end)
    return [n for n in full_series if end >= n >= start]
