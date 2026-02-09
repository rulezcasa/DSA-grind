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
    
    