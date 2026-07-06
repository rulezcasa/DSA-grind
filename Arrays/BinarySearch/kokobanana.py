'''
KOKO EATING BANANAS

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
'''

'''
APPROACH

Core idea : 
- Maximum value of k is max(piles) beacause eating anything more than that is just a waste
- Minimum value of k is 1 as it's a perfect valid quantity to eat per hour
- Check the minimum possible target value between min and max

- Brute Force 
1. Initialize max_value as max(piles)
2. Iterate k from 1 to max_value
    - let hours = 0 (to compute hours consumed for every k)
    - Iterate over piles and compute the hours consumed for pile i.e math.ceil(pile/k) and add it the hours variable
    - If hours lesser than or equal to hours allowed, all bananas have been consumed to resturn k. Otherwise continue to the next value of k
(Since we are doing this sequentially, from 1 to max(piles), the first succesfull return will be the least value satisfying the condition).

- Optimal
1. Initialize left as max(piles) and min as 1.
2. As long as left doesn't overlap right 
    - find mid_value as (left+right)//2 and also initialize hours as 0
    - Check for current mid_value the hours consumed
    - If hours consumed is less than or equal to hours allowed (going higher than mid isnt needed, so look into the left half -> right=mid_value)
    - If hours consumed is more than hours allowed (we need high k values to reduce the hours, so look into the right half -> left=mid_value+1)
    - Repeat till it converges to the optimal value
4. Return left which holds the least k value satisfying the condition
'''

from typing import List
import math

# Time complexity : O(MxN) where M is range (min,max) and N is the size of array
# Space complexity : O(1)
def minEatingSpeed(piles: List[int], h: int) -> int:
    max_value=max(piles)
    for k in range(1,max_value+1):
        hours=0

        for pile in piles:
            hours += math.ceil(pile / k)
        
        if hours<=h:
            return k

print(minEatingSpeed(piles = [30,11,23,4,20], h = 6))

# Time complexity : O(NlogM) where M is range (min,max) and N is the size of array
# Space complexity : O(1)
def minEatingSpeed(piles: List[int], h: int) -> int:
    right=max(piles)
    left=1
    while left<right:
        mid_value=(left+right)//2
        hours=0
        for pile in piles:
            hours+= math.ceil(pile/mid_value)
        
        if hours<=h:
            right=mid_value 
        else:
            left=mid_value + 1 # Failed for hours lesser than and EQUAL TO mid value i.e line 69. so + 1 to check ahead of mid value.
    
    return left

print(minEatingSpeed(piles = [30,11,23,4,20], h = 6)) 



        