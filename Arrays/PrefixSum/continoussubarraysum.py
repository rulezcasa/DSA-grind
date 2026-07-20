'''
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
'''

'''
APPROACH :
The idea is if prefix[i]%k=prefix[j]%k, the sum of array[i:j] (both inclusive) is a multiple of k
1. Initialize a hashmap to store remainders as keys and indices as values (wth 0:-1)
2. Initialize a running_sum variable to calculate prfix sums
3. Iterate over the nums array:
    - compute the running_sum as running_sum+=num
    - compute remainer for each running_sum (%k)
    - if remainer is already in the hashmap 
        - check if the array size in between is >=2 and if yes
            - return True
    - Otherwise, add the new remainder to the hashmap
'''

from typing import List

# Time complexity : O(N)
# Space complexity : O(min(N,k))
def checkSubarraySum(nums: List[int], k: int) -> bool:
    remainder_to_index = {0: -1} 
    running_sum = 0

    for i, num in enumerate(nums):
        running_sum += num
        remainder = running_sum % k

        if remainder in remainder_to_index:
            if i - remainder_to_index[remainder] >= 2:
                return True
        else:
            remainder_to_index[remainder] = i

    return False



    
