def move_zero_brute(arr):
    temp=[]
    count=0
    for i in arr:
        if i!=0:
            temp.append(i) #if element is non zero, append to empty array one by one in order
        else:
            count+=1 #if element is zero keep a counter for number of zeroes to be appended in the end
    for i in range(0,count):
        temp.append(0)  # Append count number of zeroes in the end
    return temp

def move_zero_optimal(arr):
    #iterate pointer i over the array
    for i in range(0,len(arr)): 
        
        #Condition to ensure next pointer (j) does not overshoot the length of the array
        if(i!=len(arr)-1):
            j=i+1
        
        #If i encounters a zero and j is non zero, swap elements
        if(arr[i]==0 and arr[j]!=0):
            if(i!=len(arr)-1):
                j=i+1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        
        #If i encounters a zero and j is also zero, look ahead for the next element
        if(arr[i]==0 and arr[j]==0):
            if(j!=len(arr)-1):
                j=j+1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    
    return arr



arr=[1,2,0,4,0,5]
output_arr=move_zero_optimal(arr)
print(output_arr)




# INPUT : arr=[1,2,0,4,0,5]
# OUTPUT : arr=[1,2,4,5,0,0]