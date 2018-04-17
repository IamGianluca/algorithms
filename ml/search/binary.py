def binary_search(L, v):
    """ (list, object) -> int

    Precondition: L is sorted from smallest to largest, all the items in L can
      be compared to v.

    Return the index of the first occurrence of v in L, return -1 if v is not
      in L.

    :param L: list we want to scan
    :param v: element we want to search within L
    """

    b = 0
    e = len(L) - 1

    while b <= e:
        m = (b + e) // 2
        if L[m] < v:
            b = m + 1
        else:
            e = m - 1

    if b == len(L) or L[b] != v:
        return -1
    else:
        return b
