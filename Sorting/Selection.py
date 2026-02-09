def selection(arr):
    for i in range(0,len(arr)): #Outer range size, increments by 1 for every iteration sorting from left
        min_idx=i
        for j in range(min_idx,len(arr)): #Inner loop to find the true minimum element and swap with minimum index element
            if (arr[j]<arr[min_idx]):
                temp=arr[min_idx]           #Swap logic using a temporary variable
                arr[min_idx]=arr[j]         
                arr[j]=temp
    return arr


def main():
    arr=[3,7,6,8,2,1]
    print(f"Unsorted array is {arr}\n")
    sorted_arr=selection(arr)
    print(f"Sorted array is {sorted_arr}")

main()

