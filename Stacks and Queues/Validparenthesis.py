'''
VALID PARENTHSIS

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

'''
APPROACH
1. Initialize a mapping (opening:closing)
2. Initialize a stack
2. Iterate over the given string
    - If ch in map, then append (i.e opening bracket)
    - If ch is map[stk[-1]] (i.e incoming character is the closing of the top character in stack (-1 index)), then pop other return False
3. Finally if the stack is empty, it's a valid parenthesis, return True otherwise false

'''

def isValid(self, s):
    map={'(':')','{':'}','[':']'}
    stk=[]

    for ch in s:
        if ch in map:
            stk.append(ch)
        elif stk and map[stk[-1]]==ch:
            stk.pop()
        else:
            return False
        
    return len(stk)==0