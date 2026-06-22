'''
REMOVE DUPLICATES FROM SORTED SORTED ARRAY - 2

Given an interger array nums sorted in ascending order, remove some duplicates in place such that each unique element appears at most twice.
The relative order of elements should be kept the same.

(Since in some languages, it's impossible to dynamically change the size of the array, store the result in the first k elements of the array)

return the k elements as array
'''

'''
APPROACH

- Brute force:
1. Initialie a freqmap to keep track of element frequencies
2. Initialize another array to store the result
3. Iterate over nums and if num part of freqmap increment by 1 otherwise default to 0 and increment by 1
    - if frequency of number is <=2 it's valid so we append to the result list 
4. Return the result list

- Two pointer: (everything before write is valid, we verify with read and see if it should be accepted or skipped)
1. If nums is an array of size 2 or lesser, just retun the length (edge case)
2. initialize write = 2 and run a loop iterateing read from 2 to length of array.  
    - If value of read and write-2 are not the same (read is the third incoming element, we are checking that with second before element, if same cant be accepted),
        - make value of write the value of read (i.e accept that element and repalce it by one position).
        - increment write by 1
3. Return write (this wholds the count of accepted elements, there by the required answer) 

'''

# Time complexity : O(N)
# Space complexity : O(N)
from typing import List
# def removeDuplicates(nums: List[int]) -> int:
#     freqmap={}
#     result=[]
#     for num in nums:
#         freqmap[num]=freqmap.get(num,0)+1

#         if freqmap[num]<=2:
#             result.append(num) 
    
#     return result

# print(removeDuplicates([1,1,1,2,2,3]))

# Time complexity : O(N)
# Space complexity : O(1)
def removeDuplicates(nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    write = 2

    for read in range(2, len(nums)):
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

    return write

print(removeDuplicates([1,1,1,2,2,3]))


        

