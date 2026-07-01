'''
SEARCH INSERT POSITION

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

'''
APPROACH

- Brute force approach
1. Iterate over nums
    - If value at i is greater than or equal to target (then return that index i.e if equal, then target found. If greater, then it needs to be inserted there)
2. If none of the above cases, it's to be inserted in the end, so return len(nums)

- Optimal
1. initialize left and right pointers to extremes.
2. While left <=right 
    - compute mid as (left+right)//2
    - if value of mid is equal to target, then return the index (i.e mid)
    - if value of mid less than target, then target is/inserted in the right half, so move left pointer to mid+1 (mid+1 since we have already handled the mid==target case)
    - if value of mid greater than target, then targret is/inserted in the left half, so move right pointer to mid-1 (mid-1 since we have already handledthe mid==target case)
3. Return left (this will be the position where target is found or to be inserted as, everything to the right is greater than target and everything to the left is lesser than target)
'''

from typing import List

# Time complexity : O(N)
# Space complexity : O(1)
def searchInsert(nums: List[int], target: int) -> int:
    for i in range(0,len(nums)):
        if nums[i]>=target:
            return i
    return len(nums)

print(searchInsert(nums = [1,3,5,6], target = 7))

# Time complexity : O(logN)
# Space complexity : O(1)
def searchInsert(nums: List[int], target: int) -> int:
    left=0
    right=len(nums)-1
    while left<=right: # equal to So that elements can be inserted in the end as well (last position)
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            left=mid+1
        if nums[mid]>target:
            right=mid-1
    return left

print(searchInsert(nums = [1,3,5,6], target = 7))




