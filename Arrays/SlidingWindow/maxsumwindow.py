'''
Given an array nums and an integer k, find the maximum sum of any contiguous subarray of size exactly k.
Example: nums = [2, 1, 5, 1, 3, 2], k = 3 → Output: 9 (subarray [5,1,3])
'''
'''
APPROACH 
1. Initialize running_sum=0
2. Calculate running_sum for the first k elements and store it (which is also the max_sum to begin with)
3. Iterate left from 1(already calculated from 0 to k) uptill len(nums)-k+1 (the point till which 3 elements can be captured ahead without runniing out of index)
    - dynamically compute right as left+k-1
    - subtract the leaving element and add the incoming element onto running_sum
    - whichever is greater (max_sum, running_sum), that stays max_sum
4. Return max_sum
'''

from typing import List

# Time complexity : O(N)
# Space complexity : O(1)
def maxsum(nums : List[int], k: int):
    running_sum=0
    for num in range(0,k):
        running_sum+=nums[num]
    max_sum=running_sum
        
    for left in range(1, len(nums)-k+1):
        right=left+k-1
        running_sum-=nums[left-1]
        running_sum+=nums[right]
        max_sum=max(max_sum,running_sum)
    
    return max_sum


print(maxsum(nums = [4,4,4,4], k=2))