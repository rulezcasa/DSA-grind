'''
REVERSE LINKED LIST 

Given a singly linked list, reverse it and return
'''

'''
APPROACH  :
Track the previous node (which will become next when reversing)
Also track the next node (which stores the remaining list)
1. Initialize previous=None (starting node)
2. Initialize current=head
3. While current: (i.e while current doesnt reach end of list)
    3.1 Store the next_node (current.next)
    3.2 Mark current.next as previous (reversal)
    3.3 Mark previous as current (for the next iteration, the current nodes becomes the previous)
    3.4 Mark current as new_node
4. This repeats and return previous
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        previous=None
        current=head
        while current:
            next_node=current.next
            current.next=previous
            previous=current
            current=next_node
        return previous
        