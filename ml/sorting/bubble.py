import copy


def bubble_sort(l):
    """Sort list from smallest to largest using bubble sort algorithm.

    Args:
        l (list): unsorted list.

    Return:
        list: Sorted list.
    """
    target = copy.copy(l)
    begin, end = 0, len(target) - 1

    while end != 0:
        for i in range(end):
            if target[i] > target[i + 1]:
                target[i], target[i + 1] = target[i + 1], target[i]
        end -= 1
    return target
