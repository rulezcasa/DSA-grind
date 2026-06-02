'''
REVERSE NUMBER
'''

'''
APPROACH
- split the digits by mod 10
- add the digit to the reversed number by multiplying by 10 (to keep place values in order)
- floor divide the number by 10 to keep only the remaining digits
'''

def reverseNumber(n,revn):
    while n>0:
        digit=n%10
        revn=(revn*10)+digit
        n=n//10
    
    return revn

if __name__=="__main__":
    n=int(input("Enter number"))
    revn=0
    output=reverseNumber(n,revn)
    print(f"Reversed number is:{output}")
    
    