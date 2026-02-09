'''
FIND THE DUPLICATE NUMBER

1. Given an array of integers 'nums' containing n+1 integers where each integer is in the range [1,n] (i.e repetition is guaranteed)
2. There is only ONE repeated number in nums, return this repeated number
3. You must solve the problem without modifying the array nums and uses only constant extra space
'''

'''
 APPROACH 

 - Identify it to be LinkedList problem and the cycle 

    i.e say array =[1,3,4,4,2], the each node points to the index = value of the node
        indices : (0) -> (1) -> (3) -> (4) -> (2) -> (4) -> ...
        values : 1 -> 3 -> 4 -> 2 -> 4 -> 2 -> ....

   (4) -> (2) -> (4) is a cycle here

- Floyd's algorithm

    Step 1 : Indentify the cycle 

        1. Initialize two points 'slow' and 'fast' to the head
        2. slow will move one step at a time and fast will more two steps at a time
        3. check if at any point, they point to the same node before reaching null
        4. if yes, cycle exists otherwise no cycle

    Step 2 : Idenitfy the starting point of the cycle (result)

        1. Keeping the fast point as it is, reset the slow pointer to the head
        2. Move both pointers one at a time
        3. The point that they meet will be the starting point of the cycle
'''

class Solution:
    def findDuplicate(self, nums):
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        
        slow=0
        while True:
            slow=nums[slow]
            fast=nums[fast]
            if slow==fast:
                break
        return slow
    
nums=[1,3,4,4,2]
sol=Solution()
print(sol.findDuplicate(nums))
