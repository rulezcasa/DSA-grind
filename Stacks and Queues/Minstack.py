'''
MIN STACK
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

'''
APPROACH (Maintain another stack whose top maintains the minimum value corresponding to position of the main stack i.e say stk[3], minstk[3] is the minmum value in that position)
1. Initialize stk and minstk
2. Implement push :
    - append value in stk
    - if minstk is empty, just append the value otherwise, append min(minstk[-1],value)
3. Implement pop :
    - Pop from stk
    - Pop from minstk
4. Implement top:
    - stk[-1]
5. Implement minstk:
    - Return minstk[-1]
'''

class MinStack(object):

    def __init__(self):
        self.stk=[]
        self.minstk=[]
        
    def push(self, value):
        self.stk.append(value)
        if not self.minstk:
            self.minstk.append(value)
        else:
            self.minstk.append(min(value,self.minstk[-1]))

    def pop(self):
        self.stk.pop()
        self.minstk.pop()

    def top(self):
        return self.stk[-1]
        
    def getMin(self):
        return self.minstk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()