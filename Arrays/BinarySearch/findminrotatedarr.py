'''
FIND MINUMUM IN ROTATED SORTED ARRAY

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

'''
APPROACH

- Brute force approach:
1. Declare a min_num variable which is the maximum possible value
2. Iterate num over the array
    - If num is lesser than min_num, update min_num to num
3. Finally return min_num

- Optimal
1. Declare left and right pointers to extremes.
2. while left is lesser than right:
    - compute mid as (left+right)//2
    - if value of mid is greater than value of right 
        - move left to the starting of the right half (the idea is that, if mid is greater than right, then obviously the minimum cannot be in the left half
                                                        because its not sorted)
    - if value of mid is lesser than value of right (minimum is in the left half or it can be mid itself)
        - right = mid
3. return nums[left]

'''

from typing import List

# Time complexity : O(N)
# Space complexity : O(1)
def findMin(nums: List[int]) -> int:
    min_num=float('+inf')
    for num in nums:
        if num<min_num:
            min_num=num
    return min_num

print(findMin([11,13,15,17]))


# Time complexity : O(N)
# Space complexity : O(1)
def findMin(nums: List[int]) -> int:
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right)//2
        if nums[mid]>nums[right]:
            left=mid+1
        if nums[mid]<nums[right]:
            right=mid
    return nums[left]


print(findMin([11,13,15,17]))

