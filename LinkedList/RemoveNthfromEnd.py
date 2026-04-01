'''
REMOVE NTH NODE FROM END OF LINKED LIST

APPROACH : TWO POINTER

1. Initialize slow and fast pointers to head
2. Move the fast pointer ahead by n nodes
3. Now untill end of list, move slow and fast pointers one node at a time.
4. Since there is a gap of n nodes constantly maintained between fast and slow pointer, the slow pointer will point at the node to be removed
5. Remove that node by tracking a previous.
6. Edge case : if there is only one node, returnz None directly
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow,fast=head,head
    prev=slow
        
    for _ in range(n):
        fast = fast.next

    if fast is None:
        return head.next

    while fast is not None:
        prev=slow
        slow=slow.next
        fast=fast.next

    prev.next=slow.next
    return head

            
        







        
        