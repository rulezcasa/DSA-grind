'''
COUNT DIGITS
'''

'''
APPROACH

- Iterate over the number untill it's greater than 0
- for every iteration step increment count by 1
- update number by removing one digit by using floor division by 10
- Finally, return the count
'''


def countdigits(N):
    count=0
    while(N>0):
        count=count+1
        N=N//10
    return count

print(countdigits(135))