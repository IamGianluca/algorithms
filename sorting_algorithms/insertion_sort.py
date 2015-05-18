def insert(L, i):
    """ (list, int) -> NoneType

    Precondition: L[:i] is sorted from smallest to largest

    Move L[i] on where it belongs in L[:i+1]

    :param L: unsorted list
    :param i: index of first unsorted element

    >>> L = [3, 5, 7, 1]
    >>> insert(L, 3)
    >>> L
    [1, 3, 5, 7]
    """

    length = len(L[:i])

    # The value to be inserted into the sorted part of the list
    value = L.pop(i)

    # Find the index, j, where the value belongs
    j = i
    for n in reversed(range(length)):
        if value < L[n]:
            j = n

    # Insert value where it belongs and shift to the right the other values
    L.insert(j, value)


def insertion_sort(L):
    """ (list) -> NoneType

    Sort the items of L from smallest to largest

    :param L: unsorted list

    >>> L = [2, 5, 9, 1]
    >>> insertion_sort(L)
    >>> L
    [1, 2, 5, 9]
    """

    length = len(L)

    for i in range(length):
        insert(L, i)


if __name__ == '__main__':
    import doctest
    doctest.testmod()