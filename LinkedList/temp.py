class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def length(self):
        if self.head is None:
            return 0

        current = self.head
        ctr = 0
        while current is not None:
            ctr += 1
            current = current.next
        return ctr
    
    def display(self):
        if self.head is None:
            return "Empty"
        elements=[]
        current=self.head
        while current is not None:
            elements.append(current.data)
            current=current.next
        return elements

    def get(self,idx):
        if idx>self.length():
            return "List Index out of Range"
        current=self.head
        ctr=0
        while ctr!=idx:
            current=current.next
            ctr+=1
        return current.data
    
    def delete(self,idx):
        if idx>self.length():
            return "List Index out of Range"
        current=self.head
        prev=self.head
        ctr=0
        while ctr!=idx:
            prev=current
            current=current.next
            ctr+=1
        prev.next=current.next
    
    def remove_duplicates(self):
        ptr1=self.head
        while ptr1 is not None:
            prev=ptr1
            ptr2=ptr1.next

            while ptr2 is not None:
                if ptr1.data==ptr2.data:
                    prev.next=ptr2.next
                    ptr2=prev.next
                else:
                    ptr2=ptr2.next
                    prev=prev.next
            ptr1=ptr1.next


            
    
ll=LinkedList()
ll.append(3)
ll.append(5)
ll.append(3)
ll.append(9)
print(ll.display())
print(ll.get(2))
print(ll.remove_duplicates())
print(ll.display())
