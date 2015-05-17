def selection_sort(L):
    """
    :param L: unsorted list
    :return: this is a method, there is no return function. The method sorts a list using
      selection sort algorithm

    >>> L = [2, 7, 5, 3]
    >>> selection_sort(L)
    >>> L
    [2, 3, 5, 7]
    """

    end = len(L)

    # Find the index of the smallest element in L[i:] and swap that item
    #   with the item at index i
    for i in range(end):
        index_of_smallest = get_index_of_smallest(L, i)
        L[index_of_smallest], L[i] = L[i], L[index_of_smallest]


def get_index_of_smallest(L, i):
    """
    (list, int) -> int

    :param L: list we want to analyse
    :param i: index from where we want to start
    :return: index of smallest object in the list
    """

    # The index of the smallest item so far
    index_of_smallest = i
    end = len(L)

    for j in range(i + 1, end):
        if L[j] < L[index_of_smallest]:
            index_of_smallest = j

    return index_of_smallest


if __name__ == '__main__':
    import doctest
    doctest.testmod()