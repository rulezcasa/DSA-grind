'''
CONTAINS DUPLICATE

1. Given an integer array nums.
2. return true if any value appears more than once in the array. 
3. otherwise return false.
'''

'''
APPROACH

- Brute Force : Iterate over the array using a nested for loop, when and check for matches, if matched, then return True.
- Optimal : Use a hashmap and and check if for any hash value > 1. if yes, return true (works only when values are continous)

- Edge case : When values are negative or not continous it breaks, hash maps cannot be used. We use a set instead

'''

#Optimal
nums = [1, 2, 3, 3]
hasharr=[0]*len(nums)

for i in nums:
    hasharr[i]+=1

print(hasharr)

for i in hasharr:
    if i>1:
        print("Duplicate element found")


# Edge case - Negative values or non - continous
nums = [1, 2, -3, -3]
seen=set()
for i in nums:
    if i in seen:
        print("Duplicate element found")
    else:
        seen.add(i)