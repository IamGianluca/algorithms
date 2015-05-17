def linear_search(L, v):
    """
    (list, object) -> int

    Return the index of the first occurrence of v in L, if there is one. If v is not
      in L, then return -1

    >>> linear_search([2, 3, 5, 7], 2)
    0
    >>> linear_search([2, 3, 5, 7], 5)
    2
    >>> linear_search([2, 3, 5, 7], 9)
    -1
    """

    i = 0
    length = len(L)

    while i != length and L[i] != v:
        i += 1

    if i == length:
        return -1
    else:
        return i

if __name__ == '__main__':
    import doctest
    doctest.testmod()