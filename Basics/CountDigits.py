def countdigits(N, count):
    while(N>0):
        count=count+1
        N=N//10
    return count

if __name__=="__main__":
    count=0
    N=int(input("Enter integer"))
    digits=countdigits(N, count)
    print(f"Number of digits in {N} is", digits)