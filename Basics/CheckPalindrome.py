'''
CHECK PALINDROME

Palindrome : A number that is equal to the number when reversed
'''

'''
APPROACH 

- Reverse the number by iterating till number is greater than 0
    - split the digits by mod 10
    - add the digit to the reversed number by multiplying by 10 (to keep place values in order)
    - floor divide the number by 10 to keep only the remaining digits
- If reversed number is equal to the original number, than it's a palindrome
'''

def check_plaindrome(num):
    number=num
    revn=0

    #reverse number
    while num>0:
        digit=num%10
        revn=(revn*10) + digit
        num = num // 10
    
    if revn==number:
        print("is palindrome")
    else:
        print("is not plaindrome")

check_plaindrome(111)