'''
VALID ANAGRAM

- s said to be an anagram of t, if both have the exact same characters but are allowed to be shuffed in order
'''

'''
APPROACH

- Using Hashmaps
1. Initialize two hashmaps to count frequency of each character in string t and s respectively.
2. Compare the frequency of characters in each of the hashmaps, if same, then it's an anagram

'''

#Inputs
s="racecr" 
t="carrace"
# Initializing hashmaps
counts, countt = {}, {}

for i in s:
    counts[i]=1+counts.get(i,0) # .get checks for that key, if not present uses a default like 0 here. 

for i in t:
    countt[i]=1+countt.get(i,0) # .get checks for that key, if not present uses a default like 0 here.

# # Compare frequencies
# for char in counts:
#     if counts[char]!=countt.get(char,0):
#         print("Is not Anagram")
        
# # Suppose there are extra characters in s!=t i.e there are extra characters in t, we check against t as well.
# for char in countt:
#     if countt[char] != counts.get(char, 0):
#         print("Is not Anagram")


# Simpler : Python dictionaries can be compared directly
if counts!=countt:
    print("Is not Anagram")


