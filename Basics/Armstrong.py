def checkArmstrong(n):
    length=len(str(n))
    sum=0
    while n>0:
        digit=n%10
        sum=sum+(digit**length)
        n=n//10
    return sum
    
if __name__=="__main__":
    n=int(input("Enter number"))
    sum=checkArmstrong(n)
    if(sum==n):
        print("Inputted number is an armstrong!")
    else:
        print("Inputted number is not an armstrong!")


#Time complexity ; O(logn+1)

