'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
'''
'''
THE MATH:
- Say the starting and ending indices of the subarray whose sum=k is l and r.
- The subarray sum is nothing but nums[l]+nums[l+1]+....+nums[r].
- Using prefix sums : subarray_sum=prefix[r]-prefix[l-1]
- We are checking if prefix[r]-prefix[l-1]=k
- Rearranging : prefix[l-1]=prefix[r]-k (essentially, for a given step, we minus k and check if that value was encountered before)
- If yes, that subarray is valid.
'''

'''
APPROACH:
1. Initialize prefix_sum and count variables to 0
2. Initialize a dictionary with 0 as the first key with frequency value 1 (default start)
3. Iterate overnums and compute prefix_sum:
    - increment the value of count by the frequency value of prefix_sum-k, (if not present it's 0+1=1)
    - Now add/increment the current prefix_sum to the dictionary
4. Return count

'''

from typing import List

# Time complexity : O(N)
# Space complexity : O(N)
def subarraySum(nums: List[int], k: int) -> int:
    prefix_sum = 0
    count = 0

    # prefix_sum -> frequency
    freq = {0: 1}

    for num in nums:
        prefix_sum += num

        # Add the number of previous prefix sums equal to (prefix_sum - k)
        count += freq.get(prefix_sum - k, 0)

        # Record the current prefix sum
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count

print(subarraySum(nums = [1,2,3], k = 3))


