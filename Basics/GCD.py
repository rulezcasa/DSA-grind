def findGCD(divisor,dividend):
    if(divisor)==0:
        return dividend
    rem=dividend%divisor
    return findGCD(rem,divisor)

if __name__=="__main__":
    n1=int(input("Enter first number"))
    n2=int(input("Emter second number"))
    if n1>n2:
        gcd=findGCD(n2,n1)
    else:
        gcd=findGCD(n1,n2)
    print(f"The GCD of {n1} and {n2} is :",gcd)