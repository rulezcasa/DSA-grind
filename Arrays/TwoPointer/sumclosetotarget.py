'''
You are given a sorted array of unique integers arr and a target integer. Find the pair of elements in arr whose sum is closest to target (not necessarily equal). 
Return the pair of values (a, b) that achieves the closest sum. If there's a tie (two pairs equally close), return either.
'''

'''
APPROACH
1. Intialize left and right to 0 and len(nums)-1 respectively
2. Initialize current difference as 0 and current_pair=(0,0)
3. As long as left doesn't cross right (left<right):
    - if sum of values of left and right is greater than target
        - decrement right (to decreaese the sum)
        - Also check, if running_difference (target-sum) < current_difference (that means, its closer to target)
        - Then update, current_difference=running_difference and current_pair as (nums[left],nums[right])
    - if sum of values of left and right is lesser than target
        - increment left (to incease sum)
        - Also check, if running_difference (target-sum) < current_difference (that means, its closer to target)
        - Then update, current_difference=running_difference and current_pair as (nums[left],nums[right])
    - If sum of values of left and right is matching the target (that is the closest possible, i.e difference=0)
        - so just return [nums[left],nums[right]]
4. Return current_pair
'''

from typing import List

# Time Complexity : O(N)
# Space complexity : O(1)
def find_closest_sum(nums : List[int], target) -> List[int]:
    left=0
    right=len(nums)-1
    current_difference=float('inf')
    current_pair=(0,0)
    while left<right:
        if nums[left]+nums[right]>target:
            running_difference=(abs(target-(nums[left]+nums[right])))
            if running_difference < current_difference:
                current_difference=running_difference
                current_pair=(nums[left],nums[right])
            right-=1

        elif nums[left]+nums[right]<target:
            running_difference=(abs(target-(nums[left]+nums[right])))
            if running_difference < current_difference:
                current_difference=running_difference
                current_pair=(nums[left],nums[right])
            left+=1
        else:
            current_pair=(nums[left],nums[right])
            return current_pair
    
    return current_pair

        
print(find_closest_sum(nums = [1, 2, 3, 4, 5], target = 5 )) 

