'''
MAXIMUM SUBARRAY

Given an integer array nums, find the subarray with the largest sum, and return its sum. 
'''

'''
APPROACH

- Brute force approach ;
1. Run nested loops, i.e fix element and iterate from there to end
2. Increment sum and compare with max and update
3. When the outer loop incremements, make sum 0 (start as fresh subarray)
4. Return Max

- Kadane's algorithm:
1. Iterate over the array and increment sum with the element
2. At each step, compare with maximum and update
3. Also, if the running sum is negative, just make it 0 (negative running sum can never lead to a bigger subarray, so can be 0)
4. Return Max

'''



from typing import List

#Brute force

# Time complexity : O(N^2)
# Space complexity : O(1)

def max_subarray(nums=List[int]) -> int:
    max=float('-inf')
    for i in range(0,len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum=sum+nums[j]
            if sum>max:
                max=sum
    return max

print(max_subarray([5,4,-1,7,8]))


# Kadan's algorithm

# Time complexity : O(N)
# Space complexity : O(1)

def max_subarray(nums):
    sum = 0
    max_sum = float('-inf')

    for num in nums:
        sum += num

        max_sum = max(max_sum, sum)

        if sum < 0:
            sum = 0

    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))







