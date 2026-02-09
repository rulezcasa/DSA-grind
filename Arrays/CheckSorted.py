# #Optimal approach
# def checksorted(arr):
#     flag=False
#     for i in range(0,len(arr)-2):
#         if arr[i+1]>=arr[i]:
#             flag=True
#         else:
#             flag=False
#     return flag
        

#brute force approach
def checksorted(arr):
    flag=True
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                flag=False
    return flag


arr1=[1,2,3,4,5,6]
arr2=[4,8,3,9,2,1]
checksorted1=checksorted(arr1)
checksorted2=checksorted(arr2)

if checksorted1:
    print("arr 1 is sorted")
else:
    print("arr 1 is not sorted")

if checksorted2:
    print("arr 2 is sorted")
else:
    print("arr 2 is not sorted")