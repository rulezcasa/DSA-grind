def checkPrime(n):
    flag=False
    if(n>0):
        if(n==2):
            flag=True
        for i in range(2,n):
            if((n%i)==0):
                print("It is not a prime number")
                break
            else:
                flag=True
    if(flag):
        print("It is a prime number")

if __name__=="__main__":
    checkPrime(14)
