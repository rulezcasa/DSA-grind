'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

'''
APPROACH (write holds the end of valid sequence and read checks for zerooes, if present skip and pull back the next non zero elemnet)
(overall goal is to bring the non zero elements to front and fill remaining spots with zeroes)
1. Initilize write to index 0
2. Iterate read from 0 to length of nums
    - if value of read is not equal zero (accept the element)
        - make value of write the value of read (basically skip elements in between which are zeroes)
        - increment write (everything before write is valid)
3. As long as write is less than len(nums):
    - fill in with zeroes and increment write

'''

from typing import List


def moveZeroes(nums: List[int]) -> None:
    write=0

    for read in range(0,len(nums)):
        if nums[read]!=0:
            nums[write]=nums[read]
            write+=1
    
    while write<len(nums):
        nums[write]=0
        write+=1
        

