'''
CHECK IF LINKEDLIST IS PALINDROME

APPROACH : TWO POINTER

- Identify the middle of the LinkedList

    1. Initialize one slow and fast pointer to head
    2. Move slow pointer by 1 node and fast pointer by 2 nodes till the end
    
    The slow pointer will poiint at the middle node at the end traversal

- Reverse the second half of LinkedList

    1. Initilize current to pointing node (slow) and prev to None
    2. as long as current is valid:
        2.1. Store the next node in nxt
        2.2. Reverse the link i.e curr.next will point the prev
        2.3. Move prev forward i.e prev will become curr
        2.4. Move curr forward i.e curr will become nxt
        
        now prev points to the head of second half

- Compare the first half and second half element by element 
    1. Initialize first and second to heads of first and second half respectively
    2. Being traversing, as long as first and second half elements remain the same, return True (palindrome) otherwise False (not plaindrome)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def isPalindrome(self, head: Optional[ListNode]) -> bool:
    slow,fast=head,head
    while fast and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        
    curr=slow
    prev=None

    while curr:
        nxt=curr.next 
        curr.next=prev 
        prev=curr
        curr=nxt

    #Compare halves     
    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True



