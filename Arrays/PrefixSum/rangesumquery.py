'''
RANGE SUM QUERY

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''
'''
APPROACH : Assume that this object is called multiple times togther, so efficient way to do this would be have the prefix sums for each index ready.
1. Define a function to compute prefix sums :
    - initialize prefix sum list and running_sum=0
    - iterate across nums and increment the running_sum by index value
    - Append this value to the list (the prefix sum list will hold the sum uptill the current index for all indices)
2. Call the above function in the constructor itself to compute sums and have it ready
3. initialize summ=0
4. If left = 0. summ is just prefixsums[right]
5. Otherwise, summ is prefixsums[right]-prefixsums[left-1] (left-1 becasue we remove only the part before left, as left is inclusive)
5. Return summ
'''

from typing import List

# Time complexity : O(N) (building the prefix sum) and O(1) (pulling out the sum for the range)
# Space complexity : O(N) (building the prefix sum) and O(1) (pulling out the sum for the range)

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.prefixsums=[]
        self.computeprefixsums()
    
    def computeprefixsums(self):
        running_sum=0
        for num in self.nums:
            running_sum+=num
            self.prefixsums.append(running_sum)    

    def sumRange(self, left: int, right: int) -> int:
        summ=0
        if left==0:
            summ=self.prefixsums[right]
        else:
            summ=self.prefixsums[right]-self.prefixsums[left-1]
        return summ


nums = [1, 2, 3, 4, 5]

obj = NumArray(nums)

print(obj.sumRange(0, 0))  # 1
print(obj.sumRange(4, 4))  # 5
print(obj.sumRange(0, 4))  # 15
print(obj.sumRange(1, 3))  # 9
print(obj.sumRange(2, 4))  # 12