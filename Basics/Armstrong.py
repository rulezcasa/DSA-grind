'''
CHECK IF NUMBER IS ARMSTRONG

Armstrong : Numbers whose sum of digits raised to the power of the number of digits is equal to the number itself

153 = 1^3 + 5^3 + 3^3 = 153
'''

'''
APPROACH :
- Find the length of the number (this is the power to be raised).
- Iterate till num is greater than 0:
    - split digits by mod 10 
    - raise the digit to the power of length and add it to the sum
    - update num to the remaining digits only (floor divison)
- if the sum is equal to the original number, then its armstrong
'''

def checkArmstrong(n):
    length=len(str(n))
    sum=0
    while n>0:
        digit=n%10 # Modulus : returns the remainer
        sum=sum+(digit**length)
        n=n//10 # Floor division : returns the quotient without remainder 
    return sum
    
if __name__=="__main__":
    n=int(input("Enter number"))
    sum=checkArmstrong(n)
    if(sum==n):
        print("Inputted number is an armstrong!")
    else:
        print("Inputted number is not an armstrong!")


#Time complexity ; O(logn+1)



