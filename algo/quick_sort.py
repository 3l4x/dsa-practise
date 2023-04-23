"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array)<=1:
        return array
    max_length = len(array)
    pivot = array[max_length//2]
    left = [ x for x in array if x < pivot]
    middle = [ x for x in array if x == pivot]
    right = [ x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print(quicksort(test))