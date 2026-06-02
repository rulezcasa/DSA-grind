def rotate_arr_right(k,arr):
    temp=[0]*len(arr) 
    temp[:k]=arr[-k:] #copy last k elements to first of temp array
    for i in range(0,len(arr)-k):
        temp[i+k]=arr[i] #shift and copy by k
    return temp

def rotate_arr_left(k,arr):
    temp=[0]*len(arr) 
    temp[-k:]=arr[:k] #copy first k element to last of temp array
    for i in range(0,len(arr)-k):
        temp[i]=arr[i+k] #shift and copy by k
    return temp
    

arr=[1,2,3,4,5]
k=2
rotated_arr_right=rotate_arr_right(k,arr)
rotated_arr_left=rotate_arr_left(k,arr)
print(f"Rotated array right by {k} positions is {rotated_arr_right}")
print(f"Rotated array left by {k} positions is {rotated_arr_left}")

