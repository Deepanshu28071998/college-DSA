def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_item
    return arr


arr = [5, 3, 2, 1, 4]
print("Unsorted Array:")
print(arr)
print("\nSorted Array:")
print(insertion_sort(arr))
