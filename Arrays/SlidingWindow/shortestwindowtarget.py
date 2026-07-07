'''
Given an array of positive integers nums and a positive integer target, find the length of the shortest contiguous subarray whose sum is greater than or equal to target. 
If no such subarray exists, return 0.
'''

'''
APPROACH (Explore using right untill condition passes, then shrink left untill condition fails to find minimum, shfit window)
1. Initialze left and running sum to 0
2. Initialize the shortest possible length to some max value
3. Iterate right over the array:
    - Add the currrent integer to the running sum
    - As long as running sum >= target:
        - Update shortest to be the minimum of shortest of right-left+1 (window size)
        - Subtract value of left pointer value (shrinking)
        - One check here is if left==right, just break the loop otherwise incremenet left+1 (ensuring left doesn't cross right while shrinking)
4. Return the shortest
'''

from typing import List

# Time complexity : O(N) - even though we have a while loop, but arent' backing or iterating agian, just shrinking
# Space complexity : O(1)
def shortestarr(nums: List[int], target: int) -> int:
    left=0
    shortest=float("inf")
    running_sum=0
    for right in range(0,len(nums)):
        running_sum+=nums[right]
        
        while running_sum>=target:
            shortest=min(shortest,(right-left+1))
            running_sum-=nums[left]
            if left==right:
                break
            else:
                left+=1
    
    if shortest==float("inf"):
        return 0
    else:
        return shortest

print(shortestarr(nums = [5], target = 5))

