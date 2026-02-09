def bubble(arr):
    for j in range(len(arr)-1,0,-1): #Reverse outer loop to keep the last element sorted
        for i in range(0,len(arr)-1): #Inner loop to swap neighbour elements
            if(arr[i]>arr[i+1]):
                temp=arr[i]            #Swap
                arr[i]=arr[i+1]
                arr[i+1]=temp
    return(arr)


def main(): 
    arr=[3,7,6,8,2,1]
    print(f"Unsorted array is {arr}\n")
    sorted_arr=bubble(arr)
    print(f"Sorted array is {sorted_arr}")

main()

