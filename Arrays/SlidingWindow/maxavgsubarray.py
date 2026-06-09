'''
MAXIMUM AVERAGE SUBARRAY - I

You are given an integer array nums consisting of n elements and an integer k.
Find a contigous subarray whose length is equal to k and has the maximum average value.
Return this value
'''

'''
APPROACH

- Brute force
1. Run an outer loop with i from 0 to n-k+1 (upper bound till which array size of k is maintained).
2. Run an inner loop, from i to i+k (k elements captured).
3. At each increment, calculate average and update if greater than max average.
4. Remember to reset sum to 0 for every outerloop increment (since its a fresh array).

- Sliding window (maintain a fixed sized window, as we shift, add the incoming element and remove the leading element for the updated sum)
1. run an initial loop for compute sum,average for first k elements. (initial sliding window)
2. now start another loop, where you increment the start and end pointers by 1. (end can be dynamically calc by adding k-1 to start at each step)
3. sum is nothing but : remove leaving element and add the coming element
4. Computer average for each sliding window, compare with max_avg and update
5. Return max_avg
'''

from typing import List

# Time complexity : 0(N^2)
# Space complexity : O(1)
def findMaxAverage(nums: List[int], k: int) -> float:
    max_avg=float('-inf')
    for i in range(0,len(nums)-k+1): #len(nums)-k+1 sets the upper bound till which outer loop can iterate so that inner loop mantains k length without error
        sum=0
        for j in range(i,i+k):
            sum+=nums[j]
        avg=sum/k
        max_avg=max(avg,max_avg)
    
    return max_avg

# Time complexity : 0(N)
# Space complexity : O(1)
def findMaxAverage(nums: List[int], k: int) -> float:
    sum=0
    # Initial sliding window
    for i in range(0,k):
        sum+=nums[i]
        
    max_avg=sum/k
    
    # Loop to slide the window
    for start in range(1,len(nums)-k+1): #starting from 1 as, 0 to k was computed above
        end=start+(k-1) #dynamically calculating end at every iteration from start
        sum=sum+(nums[end]-nums[start-1])  
        avg=sum/k
        max_avg=max(avg,max_avg)
    
    return max_avg


print(findMaxAverage([1,12,-5,-6,50,3],3))   