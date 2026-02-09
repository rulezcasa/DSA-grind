def findlargestrecursive(arr):
    max=0
    for i in arr:
        if i>max:
            max=i
    return max

def findlargestbrute(arr):
    arr.sort()
    return arr[len(arr)-1]

arr=[5,8,3,9,2,10]
largestbrute=findlargestbrute(arr)
largestrecursive=findlargestrecursive
print(f"largest element using bruteforce is {largestbrute}")
print(f"largest element using recursive is {largestrecursive}")