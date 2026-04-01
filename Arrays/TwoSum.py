'''
TWO SUM

- Return the indices of the two numbers in the given array such that they add up to target
- Eg. nums=[2,7,11,15] and target=9 then, output=[0,1] because nums[0]+nums[1]=9
'''

'''
APPROACH

- Brute force:
    1. Run nested loops on the array, add and check in each iteration (O(N^2)) - NOT OPTIMAL

- Hashmap :
    1. Fix one number in the array (say x)
    2. Target - x = y (y is the number we want to find)
    3. Dynamically build a hashmap by enumerating over the array :
        - check if y already exists, if yes return index of value and index of current enumeration pointer
        - else add the value to hashmap
'''

from typing import List

def twosum(nums: List[int], target: int) -> List[int]:
    hashmap={}
    for index, value in enumerate(nums): # Enumerate is used to track both indices and valuesa on an iterable.
        complement=target-value
        if complement in hashmap:
            return [hashmap[complement], index]
        hashmap[value]=index
        

print(twosum([2,7,11,15],13))
