'''
3 SUM

Given an integer array nums, return all the triplets as a list of arrays such that nums[i] + nums[j] + nums[k] == 0
'''

'''
APPROACH

- Brute force :
1. Initialize a set (so as to avoid duplicate triples)
2. Intialize a list (the return type is list)
3. Iterate i over nums from 0
    - Itearte j over nums from i+1
        - Iteraate k over nums from j+1
         - If nums[i]+nums[j]+nums[k]==0
            - add the sorted values to triples set (sorting is a normalization step such that the set will catch duplicates)
4. Add the set elements to a list and return

- Two pointer :
1. Initialize a set (so as to avoid duplicate triples)
2. Intialize a list (the return type is list)
3. Sort the list (incrementing left and right with sum comparision pointer needs an ascended list order.)
4. Iterate i over nums from 0 (i.e fixing one element and treating remaining array as a 2sum problem)
    - Initialize as left = i+1 and right as len(nums)-1 
    - As long as left and right don't cross each other (while left<right)
        - Compute sum as nums[i]+nums[left]+nums[right]
        - If sum==0
            - add the triplets to set
            - Increment left pointer and decrement right pointer (because that combination is valid and moving just one pointer wont result in a new unique value)
        - If sum<0
            - increment left pointer
        - If sum<0
            - Decrement right pointer
5. Add the set elements to a list and return
'''

# Time complexity : O(N^3)
# Space complexity : O(1)
def threeSum(nums: list[int]) -> list[list[int]]:
    triplets=set() # We are using a set, so that only unique triplets values are allowed
    triplets_list=[]
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k]==0: 
                    triplets.add(tuple(sorted([nums[i], nums[j], nums[k]]))) # Sorting it as a normlization step, so that duplciates can be detected by the set
    
    for t in triplets:
        triplets_list.append(t)
    return triplets_list

print(threeSum(nums = [-1,0,1,2,-1,-4]))
                    


# Time complexity : O(N^2)
# Space complexity : O(k) where k is size of set
def threeSum(nums: list[int]) -> list[list[int]]:
    nums=sorted(nums)
    triplets=set()
    triplets_list=[]
    for i in range(0,len(nums)):
        left=i+1
        right=len(nums)-1
        while left<right:
            sum=nums[i]+nums[left]+nums[right]
            if sum==0:
                triplets.add(tuple([nums[i],nums[left],nums[right]]))
                left+=1
                right-=1
            if sum<0:
                left+=1
            if sum>0:
                right-=1
    
    for t in triplets:
        triplets_list.append(t)

    return triplets_list


print(threeSum(nums = [-1,0,1,2,-1,-4]))



