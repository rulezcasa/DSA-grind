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
1. Initialize an empty left and right array
2. Calculate the prefix and suffix sums by iterating over nums for and update left and right arrays
3. Iterate i from 0 to n:
    - if left[i]==right[n-1-i] i.e reverse index because we iterate from end to beginning in right array
    - If the value is same, then that is the pivot index.
    - Return i other -1 if no pivot element exists.
'''
# Time complexity : O(N)
# Space complexity : O(N)
def pivotIndex(nums: List[int]) -> int:
    n=len(nums)
    left=[]
    right=[]

    running_sum=0
    for i in range(0,n):
        running_sum+=nums[i]
        left.append(running_sum)
    print(left)
    
    running_sum=0
    for i in range(n-1,-1,-1):
        running_sum+=nums[i]
        right.append(running_sum)
    print(right)

    for i in range(0,n):
        if left[i]==right[n-1-i]:
            return i
    
    return -1 # If no pivot element exists

    # Optimization tip : Instead of computing right sum and using the right array. We can just have it as the total sum - left[i]   

print(pivotIndex(nums = [1,7,3,6,5,6]))
