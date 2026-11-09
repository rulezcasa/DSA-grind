'''
ORDER LINKED LIST

You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

In the general case, label the nodes by their original zero-based positions from 0 to n - 1. After reordering, those original positions appear in this order:

[0, n-1, 1, n-2, 2, n-3, ...]

Example 1 :
Input: head = [2,4,6,8]

Output: [2,8,4,6]
'''

'''
APPROACH (combination of many things) :
- Find the middle of the linked list (fast and slow pointer) and split the list
- Reverse the second half
- Alternate and append between the two lists to get the final order (merging) 
'''

def reorderList(self, head: Optional[ListNode]) -> None:
    # splitting the list into two halves (fast and slow pointer)
    fast=slow=head
    while slow and fast.next:
        slow=slow.next
        fast=fast.next.next
    current=slow.next
    slow.next=None

    # reversing the second half
    previous=None
    while current:
        next_node=current.next
        current.next=previous
        previous=current
        current=next_node

        # Iterate over two lists and form the ordered list
        l1=head.next # we are modifying the given list in place, head already holds the first element from l1.
        tail=head
        l2=previous # previous holds the head of reversed list
        flag=l2 # flag that tracks which from which list to append (alternating)

        while l1 and l2:
            if flag==l1:
                tail.next=l1
                tail=tail.next
                l1=l1.next
                flag=l2
                continue

            if flag==l2:
                tail.next=l2
                tail=tail.next
                l2=l2.next
                flag=l1
                continue
                
        tail.next=l1 or l2
        return None





    