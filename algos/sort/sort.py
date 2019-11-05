def insertion_sort(items):
    """
    Order of
    """
    for i in range(1, len(items)):          # an array with only 1 item is always sorted by default
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:     # compare items from right to left, shift items to right as required
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key                  # place the key at appropriate position in the array


def demo():
    items = [5, 3, 6, 7, 5, 8]
    insertion_sort(items)
    print(items)
    assert items == [3, 5, 5, 6, 7, 8]


demo()
