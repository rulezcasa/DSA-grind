'''
REMOVE Nth NODE FROM END OF LINKED LIST

Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
'''

'''
APPROACH :
1. Iterate and find the length of linked list
2. Using the length, get the index to be removed from front (length - n)
3. edge case : if index=0 (first element), return head.next
4. Otherwise iterate over the list (index is one pointer ahead then current) and when index=index_to_be_removed, assign current's pointer = current.next.next
5. return head
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Finding index to remove using length
        length=0
        current=head
        while current:
            length+=1
            current=current.next
        
        index_to_remove=length-n

        # Edge case : removal of first element
        if index_to_remove==0:
            return head.next

        # Iterate and remove the corresponing element
        index=1
        current=head
        while current:
            if index==index_to_remove:
                current.next=current.next.next
                return head
            else:
                index+=1
                current=current.next
            

        
            

        