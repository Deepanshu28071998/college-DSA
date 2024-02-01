def bubble_sort(arr):
    """Sorts the given array in ascending order using the bubble sort algorithm.

  Args:
    arr: A list of elements to be sorted.

  Returns:
    A sorted list.
  """

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr


arr = [5, 3, 8, 6, 7, 2]

sorted_arr = bubble_sort(arr)

print(sorted_arr)
