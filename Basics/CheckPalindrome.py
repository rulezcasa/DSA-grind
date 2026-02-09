def reverseNumber(n,revn):
    while n>0:
        digit=n%10
        revn=(revn*10)+digit
        n=n//10
    
    return revn

def checkPalindrome(n,revn):
    if(n==revn):
        return True
    else:
        return False


if __name__=="__main__":
    n=int(input("Enter number"))
    revn=0
    revn=reverseNumber(n,revn)
    if(checkPalindrome(n,revn)):
        print("The inputted number is a palindrome!")
    else:
        print("The inputted number is not a palindrome!")    
    