'''
LINKED LIST CYCLE DETECTION

Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
'''

'''
APPROACH (Floyd's cycle detection algorithm : ptr1 moves one step whereas ptr2 moves two steps, if there is a cycle they will meet)
1. 
'''

def hasCycle(self, head: Optional[ListNode]) -> bool:
    current=ahead=head
    while ahead and ahead.next:
        current=current.next
        ahead=ahead.next.next
        if current==ahead:
            return True
    return False

