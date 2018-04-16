import copy


def selection_sort(l):
    """Sort list from smallest to largest using selection sort algorithm.

    Args:
        l (list): Unsorted list.

    Returns:
        list: Sorted list.
    """
    target = copy.copy(l)
    end = len(target)

    # Find the index of the smallest element in target[i:] and swap that item
    #   with the item at index i
    for i in range(end):
        idx_of_smallest = get_index_of_smallest(target, i)
        target[idx_of_smallest], target[i] = target[i], target[idx_of_smallest]
    return target


def get_index_of_smallest(L, i):
    """Return the index of the smallest element of L.

    Args:
        L (list): List we want to analyse.
        i (int): Index from where we want to start.

    Returns:
        int: Index of smallest element of L.
    """

    # The index of the smallest item so far
    index_of_smallest = i
    end = len(L)

    for j in range(i + 1, end):
        if L[j] < L[index_of_smallest]:
            index_of_smallest = j

    return index_of_smallest
