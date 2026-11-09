'''
MERGED TWO SORTED LINKED LIST

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.
'''

'''
APPROACH : (two pointer, where we iterate over both lists, add to merged linked list and move ahead)
1. Initilize a dummy head and a pointer tail (that points to head) i.e tail.next is equivalent to head.next
2. As long as list1 and list2 are not none :
    2.1 if list1.val is lesser, append that (tail.next same as head.next) and increment list1=list1.next
    2.2 if list2.val is lesser, append that (tail.next same as head.next) and increment list2=list2.next
    2,3 move the tail : tail=tail.next 
3. Once the loop closes, append the remaning nodes (just point to the remaning list)
4. return head.next (next becasue the first node is dummy, the first element starts from the second node)
'''

from typing import ListNode

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head=ListNode()
    tail=head

    while list1 and list2:
        if list1.val<list2.val:
            tail.next=list1
            list1=list1.next
        else:
            tail.next=list2
            list2=list2.next
        tail=tail.next

    tail.next = list1 or list2

    return head.next
