def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from index 1 (as the first element is "sorted")
        key = arr[i]  # Element to be placed at correct position
        j = i - 1

        # Shift elements of sorted part if they are greater than key
        while j >= 0 and arr[j] > key:
            temp=arr[j+1]
            arr[j + 1] = arr[j]  # Swap logic
            arr[j]=temp
            j -= 1

        arr[j + 1] = key  # Place key at the correct position

    return arr


def main(): 
    arr = [3, 7, 6, 8, 2, 1]
    print(f"Unsorted array: {arr}")
    sorted_arr = insertion_sort(arr)
    print(f"Sorted array: {sorted_arr}")

main()
