'''
BINARY SEARCH

Given an array of intergers nums which is sorted in ascending order, and an integer target, write a function to search target in nums and return its index.
If not present, return -1
'''

'''
APPROACH
- Brute force :
1. Iterate over the the list
    - If target is found, return its index, otherwise return -1

- Optimal :
1. initialize left to start and right to start and end indices respectively
2. As long as left doesn't overlap right:
    - compute mid index as (left+right)//2
    - if the mid index value is target, return it.
    - if the mid index value is greater than target (then the requried index is present in the left half)
        - bring down right, to the end of left half.
    - if the mid index value is lesser than targer (then required index is present in the right half)
        - bring up the left, to the start of right half
3. Repeat this loop and return index once found
'''


from typing import List

# Time complexity : O(N)
# Space complexity : O(1)
def search(nums: List[int], target: int) -> int:
        for index,number in enumerate(nums):
            if number==target:
                return index
            else:
                 return -1

print(search(nums = [-1,0,3,5,9,12], target = 2))

# Time complexity : O(logN)
# Space complexity : O(1)
def search(nums: List[int], target: int) -> int:
    left=0
    right=len(nums)-1
    while left<=right:
         mid=(left+right)//2
         if nums[mid]==target:
              return mid
         if nums[mid]>target:
              right=mid-1
         if nums[mid]<target:
              left=mid+1
    
    return -1


print(search(nums = [-1,0,3,5,12,13], target = 9))

        