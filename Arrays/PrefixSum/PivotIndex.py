from typing import List

'''
FIND PIVOT INDEX

- Given an array of integers nums, calculate the pivot index
- Pivot index is the index where the sum of all numbers to the left of the index is equal to the sum on the right of the index
- If index is on the left or right edge, then the sum is 0 (as there are no elements) to the left/right.
- Return the leftmost pivot index
'''

'''
APPROACH 
- Prefix Sum

1. 
'''


def pivotIndex(nums: List[int]) -> int:
    n=len(nums)
    left=[0]*n
    right=[0]*n

    for i in range(1,n):
        left[i]=left[i-1]+nums[i-1]
        
    for i in range(n-2,-1,-1):
        right[i]=right[i+1]+nums[i+1]
        
    for i in range(0,n):
        if left[i]==right[i]:
            return i


    return -1

print(pivotIndex([2,1,-1]))