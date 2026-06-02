'''
CHECK PRIME

Prime : Any number that is divisble by only itself and 1
'''

'''
APPROACH :

- 0,1 are not prime, so check if num is less that 2, and return False
- iterate from 2 to num
    - if num mod i is divisble is 0 (i.e divisble), then return False
    - otherwise, continue
- if all above cases go ahead, then return True as the number is prime


'''

def check_prime(n):
    if n < 2:
        return "Not prime"

    for i in range(2, n):
        if n % i == 0:
            return False
        
    return "Prime"


print(check_prime(14))  