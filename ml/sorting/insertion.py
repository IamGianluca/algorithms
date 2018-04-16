import copy


def insert(L, i):
    """Move i element of l, to correct place in l[:i+1].

    Note: L[:i] is sorted from smallest to largest.

    Args:
        L (list): unsorted list.
        i (int): index of first unsorted element.

    Side effects:
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
    """Sort the items of L from smallest to largest.

    Args:
        L (list): Unsorted list.

    Returns:
        list: Sorted list.
    """
    target = copy.copy(L)
    length = len(target)

    for i in range(length):
        insert(target, i)
    return target
