#Optimal approach (smart comparision - single traversal)
def find_secondlargest(arr):
    largest=arr[0]
    secondlargest=0
    for i in arr:
        if i>largest:
            largest=i
        if(i<largest and i>secondlargest):
            secondlargest=i
    return secondlargest


def find_secondsmallest(arr):
    smallest=float('inf')
    secondsmallest=float('inf')
    for i in arr:
        if i<smallest:
            smallest=i
        if i>smallest and i<secondsmallest:
            secondsmallest=i
    return secondsmallest


#Better approach (double traversal)
def find_secondlargest(arr):
    largest=arr[0]
    secondlargest=0
    for i in arr:
        if i>largest:
            largest=i
    for j in arr:
        if j>secondlargest and j<largest:
            secondlargest=j
    return secondlargest

def find_secondsmallest(arr):
    smallest=float('inf')
    secondsmallest=float('inf')
    for i in arr:
        if i<smallest:
            smallest=i
    
    for j in arr:
        if j<secondsmallest and j>smallest:
            secondsmallest=j
    return secondsmallest

#Brute force approach (sort first)
def find_secondlargest(arr):
    arr.sort()
    return arr[len(arr)-2]

def find_secondsmallest(arr):
    arr.sort()
    return arr[1]


arr1=[9,8,7,6,5,4]
arr2=[4,6,7,8,9]
secondsmall=find_secondsmallest(arr2)
secondlarge=find_secondlargest(arr1)
print(f"Second largest element: {secondlarge} \n")
print(f"Second smallest element: {secondsmall}")


