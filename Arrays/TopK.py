'''
TOP K FREQUENT ELEMENTS

- Given an integer array and an integer k
- return the k most frequent elements
- For eg : Input: nums = [1,1,1,2,2,3], k = 2 and Output: [1,2]
'''

'''
APPROACH

- Using hashmaps and sorted() function :
    1. 
'''


from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    hashmap={}
    for num in nums:
        if num in hashmap:
            hashmap[num]=hashmap[num]+1
        else:
            hashmap[num]=1

    hashmap_sorted=sorted(hashmap.items(), key=lambda item: item[1], reverse=True) #sorted() uses (nlogn) worst case time complexity, could be better.

    '''
    - hashmap.items() -> converts into list of tuples (key,value)
    - sorted() -> by default sorts it based on the first element of the tuple(key) but since we want to sort by values :
        - key=lambda item: item[1] ->  lamdba is just an anonymous function when called returns item[1] which is nothing but the value
        - reverse=True since we want it in descending order (highest to lowest)
    '''

    '''Working of lambda:
    - when sorted on X, each element of X is passed to key argument
    - So we define the key argument as a function that returns item[1] i.e the value
    '''

    #print(hashmap_sorted)

    topk=[item[0] for item in hashmap_sorted[:k]] #Pull out just the keys (item[0]) from the items of hashmap_sorted top k
    print(topk)

topKFrequent([4,1,-1,2,-1,2,3],2)




        
    