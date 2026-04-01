'''
TOP K FREQUENT ELEMENTS

- Given an integer array and an integer k
- return the k most frequent elements
'''

''

from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    hashmap={}
    for num in nums:
        if num in hashmap:
            hashmap[num]=hashmap[num]+1
        else:
            hashmap[num]=1

    print(sorted(list(hashmap.keys()), reverse=True))

    for i 
    return []


        
    