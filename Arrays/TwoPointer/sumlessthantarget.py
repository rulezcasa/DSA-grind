'''
Given an array of integers nums and an integer target, return the number of pairs (i, j) with i < j such that nums[i] + nums[j] < target.
Example: nums = [-1, 1, 2, 3, 1], target = 2 → answer: 3
(pairs: (-1,1), (-1,2), (-1,1))
'''

'''
APPROACH
1. Initialize a count variable 
2. Sort the array
3. Left = 0 and right = len(nums)-1
4. As long a left doesn't pass right (left<right):
    - if sum of values of left and right is greater than or equal to target (problem condition fails)
        - decrement right (we need to lower the sum)
    - otherwise (problem condition passes)
        - increment count by (right-left) (i.e for the selected left, right has satisifed, which also means all the values between left and right will also satisfy for right)
        - increment left by 1
5. Return count
'''

from typing import List

# Time complexity : O(nlogn)
# Space complexity : O(1)
def find_pairs(nums: List[int], target: int) -> int :
    count=0
    nums.sort()
    left=0
    right=len(nums)-1
    while left<right:
        if nums[left]+nums[right]>=target:
            right-=1
        else:
            count+=(right-left)
            left+=1

    return count


print(find_pairs(nums = [-5, -3, 0, 2, 8], target = 0))


                