class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None


    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=new_node
    
    def length(self):
        length=1
        current=self.head
        while current.next!=None:
            current=current.next
            length+=1
        return length
    
    def display(self):
        elements=[]
        current=self.head
        elements.append(current.data) #appending head data
        while current.next!=None:
            current=current.next
            elements.append(current.data)
        return elements
    
    def get(self,idx):
        if idx>=self.length():
            return "List Index Out of Range!"
        current=self.head
        ctr=0
        while ctr!=idx:
            current=current.next
            ctr+=1
        return current.data

    def delete(self,idx):
        if idx>=self.length():
            return "List Index Out of Range!"
        current=self.head
        previous=None
        ctr=0
        if idx==0:
            self.head=current.next
            return "Deleted element!\n"
        else:
            while ctr!=idx:
                previous=current
                current=current.next
                ctr+=1
            previous.next=current.next
            return "Deleted element!\n"
                
if __name__=="__main__":
    ll=LinkedList()
    elements=[1,2,3,4,5]
    for element in elements:
        ll.append(element)
    print("Elements appended succesfully!\n")
    
    print("Displaying elements :")
    print(ll.display())
    print("")

    print ("Printing length:")
    print(ll.length())
    print("")

    print("Getting element at index 2:")
    print(ll.get(2))
    print("")

    print("Deleting element at index 2:")
    print(ll.delete(2))
    print(ll.display())



    
