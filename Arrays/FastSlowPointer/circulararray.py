'''
You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move abs(nums[i]) steps backward.
Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
Every nums[seq[j]] is either all positive or all negative.
k > 1
Return true if there is a cycle in nums, or false otherwise.
'''
'''
APPROACH
1. Let n be the lenght of array
2. Define a utility function to compute the next index from a given index i : (i+nums[i])%n since the array is circular
3. iterate i over the array
    - if the value of ith index is 0 (it's already been traversed or processed), so continue
    - we track direction using signs, so if positive its one direction and if its negative its another diretion. Track the direction of i (first element for this iteration)
    - initialize slow and fast to i (slow and fast pointers start from there for this iteration)
    - while true:
        - move slow one step while checking if value of slow is a 0 (already processed) and direction is same as first element. If either fails, break
        - move fast two steps while checking if value fast is a 0 (already processed) and diection is same as second element. If either fails, break
        - if slow==fast (cycle found)
            - check the next index of slow, isnt the same as slow (i.e self loop), otherwise break from loop and return True
    - Now for this iteration, let's mark the visited elements : 
        - initialize variable curr as the value of i and as long as value of current isnt 0 (already processed) and direction is same
            - nums[curr]=0
            - update current to next index 
4. Finally return False (for all other break cases and if not retun True happened before it)
'''

from typing import List

# Time complexity : O(N)
# Space complexity : O(1)
def circularArrayLoop(nums: List[int]) -> bool:
    n = len(nums)

    def next_index(i):
        return (i + nums[i]) % n

    for i in range(n):
        # Already processed
        if nums[i] == 0:
            continue

        direction = nums[i] > 0
        slow = fast = i

        while True:
            # Move slow one step
            slow = next_index(slow)
            if nums[slow] == 0 or (nums[slow] > 0) != direction:
                break

            ## Move fast 2 steps : the reason we are doing it in 2 sepreate blocks is to check for direction and already traversed spots
            # Move fast one step
            fast = next_index(fast)
            if nums[fast] == 0 or (nums[fast] > 0) != direction:
                break

            # Move fast second step
            fast = next_index(fast)
            if nums[fast] == 0 or (nums[fast] > 0) != direction:
                break

            # Cycle found
            if slow == fast:
                # Reject self-loop (cycle length = 1)
                if slow == next_index(slow):
                    break
                return True

        # Traverse again and make the spots 0 - to mark this traversal
        curr = i
        while nums[curr] != 0 and (nums[curr] > 0) == direction:
            nums[curr] = 0 
            curr = next_index(curr)

    return False
