'''
Find the Greatest Common Divisor (GCD/HCF)

Idea : If a number divides both a and b, it must also divide the remainder when a is divided by b.
'''

'''
APPROACH :

- Divide dividend by divisor and find remainder
- Divisor becomes new dividend and remainder becomes new divisor
- Repeat untill remainder becomes 0, return the dividend which is the GCD
'''

#Iterative
def find_GCD(dividend,divisor):
    while divisor!=0:
        remainder=dividend%divisor
        dividend=divisor
        divisor=remainder
    
    return dividend

print(find_GCD(24,13))


#Recursive
def find_GCD(dividend,divisor):
    if divisor==0:
        return dividend
    remainder=dividend%divisor
    return find_GCD(divisor,remainder)

    

print(find_GCD(24,13))
