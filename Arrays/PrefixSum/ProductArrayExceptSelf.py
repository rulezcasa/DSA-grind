from typing import List

'''
PRODUCT OF ARRAY EXCEPT SELF

- Given an integer array nums.
- return an array answer such as answer[i] is the product all elements in nums except nums[i]
- For eg, Input: nums = [1,2,3,4] where Output: [24,12,8,6]
'''

'''
APPROACH 

- Using left product and right product of element at index i (Similar to prefix sum but products)
    1. Initialize a left array and right array of same size as nums
    2. Let first element of left array be 1 and last element of rigth array be 1 (since there are no elements to the left and right respectively)
    3. For left array , iterate from index 1 to end where:
        3.1 Left product at that index is product of (left array and element before that)
    4. Similarly for right array, iterate from index (len(nums)-2) to start where:
        4.1 Right product of that index is product of (right array and element after that)
    5. Final result at index i is the product of left[i] and right[i]
'''


def productExceptSelf(nums: List[int]) -> List[int]:
    left=[0]*len(nums)
    left[0]=1

    right=[0]*len(nums)
    right[len(nums)-1]=1

    answer=[0]*len(nums)

    for i in range(1,len(nums)):
        left[i]=left[i-1] * nums[i-1] #At all time left[i-1] will hold the product uptill i-1 and since we're updating that to left[i], nms[i] is excluded
    
    for i in range(len(nums)-2,-1,-1):
        right[i]=right[i+1]*nums[i+1] #At all time right[i-1] will hold the product uptill i+1 and since we're updating that to right[i], nums[i] is excluded   

    for i in range(len(nums)):
        answer[i]=left[i] * right[i]

    print(answer)

productExceptSelf([-1,1,0,-3,3])






        
        