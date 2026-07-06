'''
TWO SUM II - INPUT ARRAY IS SORTED

Given a 1 indexed array of intergers numbers that is already sorted in ascending order. Find two numbers such that they add up to the target number
Return the indices of two numbers each incremented by one, as an integer array
'''
'''
APPROACH

- Brute force :
1. Iterate i over the array
    - for a fixed i, compute the difference as target - nummbers[i] (the number that is needed to get target value)
    - iterate j over the array, if numbers[j]==difference
        - return[i+1,j+1] (incremented as the the problem requires 1-indexed)

- Two pointer approach (start with two pointers in extremes and since the array is sorted, if sum is more, move right pointer left and if less, move left pointer forward.)
1. Initialize left pointer to 0 and right pointer to len(numbers)-1 i.e extreme indices
2. While loop : left<right i.e as long as left and right pointers dont equal and overlap each other.
    - Compute the sum of values pointed by the left and right pointers, if sum==target, return [left+1,right+1] (since array is 1-indexd)
    - If sum<target, increment left pointer by 1
    - If sum>target, decrement right pointer by 1
3. Iterate til 2 sum is found

'''
from typing import List

# Time complexity : O(N^2)
# Space complexity : O(1)
def twoSum(numbers: List[int], target: int) -> List[int]:
    for i in range(0,len(numbers)):
        difference=target-numbers[i]
        for j in range(i,len(numbers)):
            if numbers[j]==difference:
                return[i+1,j+1]
        
print(twoSum(numbers = [-1,0], target = -1))


# Time complexity : O(N)
# Space complexity : O(1)
def twoSum(numbers: List[int], target: int) -> List[int]:
    left=0
    right=len(numbers)-1
    while left!=right:
        sum=numbers[left]+numbers[right]
        if sum==target:
            return[left+1,right+1]
        elif sum<target:
            left+=1
        elif sum>target:
            right-=1
        else:
            return None
    

           
print(twoSum(numbers = [2,7,11,15], target = 9))
     




[1, 2, 2, 2, 7]
