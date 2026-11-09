'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored
'''

'''
APPROACH : (Everything before write is valid, if duplicate found by comparing read and right, skip the element)
1. Initialize write to 1 (because the first element will anyway be valid - everything before write is valid)
2. Iterate read from 1 to end of array:
    - if value of read is not equal value of write - 1 (not a duplicate)
        - make nums[write]=nums[read] (accept the read value since it's not a duplicate)
        - Increment write (everything before write is kept valid)
    (if it had been equal i.e duplicate found, then write points to the duplicate element and we increment read untill a non duplicate is found and skip the duplicate elements in between)
3. Return write 
'''

from typing import List
def removeDuplicates(nums: List[int]) -> int:

    write = 1

    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return write
        

print(removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))