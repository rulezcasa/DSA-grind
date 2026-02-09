'''
DETECT CYCLE IN A LINKEDLIST

1. Given 'head' of a linkedlist
2. return true is there a cycle otherwise falst
'''

# Approach 1 : Using an additional array to keep track of nodes visited 0(N) space complexity
class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next!=None:
            slow = slow.next          # 1 step
            fast = fast.next.next    # 2 steps

            if slow == fast:
                return True

# Approach 2 : Using Flody's algorthm O(1) space complexity
class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next!=None:
            slow = slow.next         
            fast = fast.next.next    

            if slow == fast:
                return True