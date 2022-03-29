#######################################################
# Bubble sort


def bubble_sort(x) -> list:
    """bubble sort algorithm"""
    to_sort = x[:]
    i = len(to_sort)
    while i > 0:
        j = 0
        while j < i-1:
            if to_sort[j+1] < to_sort[j]:
                low = to_sort[j+1]
                to_sort[j+1] = to_sort[j]
                to_sort[j] = low
            j += 1
        i -= 1
    return to_sort

########################################################


def _split(_list):
    "Split list into two subarrays of almost half the length "
    return _list[:len(_list)//2], _list[len(_list)//2:]


def _merge(left, right):
    "merge two sorted lists"
    i = j = 0
    _list = list()

    while i < len(left) and j < len(right):
        if left[i] < right[j] :
            _list.append(left[i])
            i += 1
        else:
            _list.append(right[j])
            j += 1

    while i < len(left):
        _list.append(left[i])
        i += 1

    while j < len(right):
        _list.append(right[j])
        j += 1

    return _list


def merge_sort(_list):
    """Recursively sort the list using merge sort"""
    if len(_list) < 2:
        return _list
    left_half, right_half = _split(_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    _list = _merge(left, right)
    #print("merge \n",_list)
    return _list

########################################################
# Quick sort
def partition(_list, start, end):
    """place the pivot element such that left side contains smaller
    elements and right side contains larger"""
    pivot_index = start - 1
    pivot_value = _list[end]
    count = start
    while count < end:
        if _list[count] <= pivot_value:
            pivot_index += 1
            swap(_list, count, pivot_index,)
        count += 1
    swap(_list, end, pivot_index+1)
    #print(_list, pivot_index)
    return pivot_index


def swap(_list, x, y):
    """swap x and y index in the list"""
    _list[x], _list[y] = _list[y], _list[x]


def quick_sort(_list, start, end):
    """Recursively sort the list using quicksort"""
    if start >= end:
        return
    # if random1:
    #     index = partition1(_list, start, end)
    # else:
    index = partition(_list, start, end)

    quick_sort(_list, start, index-1)
    quick_sort(_list, index+1, end)


######################################
def insertion_sort(_list):
    """Sort the list using insertion sort"""
    for j in range(1, len(_list)):
        key = _list[j]
        i = j - 1
        while i >= 0 and _list[i] > key:
            _list[i+1] = _list[i]
            i = i-1
        _list[i+1] = key

    return _list
