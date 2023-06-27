#!/usr/bin/python3
"""Function that finds a peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """Function that finds a peak in list of unsorted integers"""

    nums = len(list_of_integers)

    if nums == 0:
        return None

    low = 0
    high = nums - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
