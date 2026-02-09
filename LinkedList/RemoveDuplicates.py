'''
You are given a singly linked list of integers.
Write a method that removes all duplicate values from the list while preserving the original order.
You must modify the list in-place.
'''

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=new_node
    
    def display(self):
        elements=[]
        current=self.head
        if current==None:
            return "Linked List Empty!"
        elements.append(current.data)
        while current.next!=None:
            current=current.next
            elements.append(current.data)
        return elements
    
    def remove_duplicates(self):
        ptr1=self.head 

        while ptr1!=None:
            prev=ptr1 #Tracking a previous node to connect with the next to next node (deletion - skipping the duplicate node)
            ptr2=ptr1.next # Pointer 2 that iterates across the LL for a fixed pointer 1

            while ptr2!=None:
                if ptr1.data==ptr2.data: # If duplicate found
                    prev.next=ptr2.next # Skip and connect the previous node to duplicate's next
                    ptr2=prev.next # Pointer 2 shifts to duplicate's next node 
                else:
                    prev=prev.next # When no match, previous node shifts to pointer 2        
                    ptr2=ptr2.next # pointer 2 goes to next. #This is the main iteration step, the previous is kept track of to delete
            ptr1=ptr1.next


    
        
ll=LinkedList()
elements=[1,2,4,3,6,5,3]
for element in elements:
    ll.append(element)

print(ll.remove_duplicates())
print(ll.display())






