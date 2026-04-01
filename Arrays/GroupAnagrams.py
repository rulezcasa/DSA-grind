'''
GROUP ANAGRAMS

- Given an array of strings, group the anagrams together in nest arrays
- Eg. Input: strs = ["eat","tea","tan","ate","nat","bat"] and Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

'''
APPROACH
- Using hashmaps and string sorting
    1. create a hashmap with defaultdict as list i.e when a not available key is accessed, an empty list against that key is created otherwise.
    2. for each string in the list :
        - sort it and check if key exists in the hashmap
        - if key exists, append the original word in the list corresponding to it
        - if key doesn't exist, default dict will automatically create a list against thay key and append the original worx
    3. All the original words are grouped as anagrams, return these values as a list.
'''
from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hashmap = defaultdict(list)  # default value is a list, if a key that is not found is accessed, it creates as empty list against that key something like .get(key,[]).
    
    for s in strs:
        sorted_s = ''.join(sorted(s))  # "eat" -> "aet"
        hashmap[sorted_s].append(s)    # append the original word against the sorted word (key), if key not present before then creates an empty list.
    
    return list(hashmap.values())  # return lists of anagrams

# Test
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


        