'''
LONGEST REPEATING CHARACTER REPLACEMENT

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase english character.
You can perform this operation at most k times.
Return the length of the longest substring containing same letter you can get after performing the above operations.
'''

'''
APPROACH

- Brute force
1. Run an outloop with i for starting of substring
2. Run an inner loop with j for end of substring, at each iteration :
    - Capture the substring
    - Count the frequency of each character (iterate over the substring)
    - Get the max frequency
    - Compute replacements needed as : Length of susbtring - maximum frequency
    - If the replacements needed is <= k, then it's valid.
    - Update max length as either the length of current substring or existing max_length
3. Return max length

- Sliding window (the idea is that we reuse stored frequencies, instead of refreshing the substring iteration):
1. Iterate over string 
    - For every character, get the frequency and increase by 1 in the hashmap
    - Compute length of substring as right-left+1
    - Get the max frequency
    - Compute replacements needed as : Length of substring - maximum frequency
    - If replacements needed is <=k, then it's valid
        - Update max length as either the length of current substring or existing max_length
    - Else (Move left pointer by 1)
        - Remove the frequency of the left pointer's character from charmap (out of window)
        - Shift left pointer by 1 i.e left+=1
    
2. Return max length
'''

"AABABBA"

# Time complexity : O(N^3)
# Space complexity : O(len(substring)), N is length of substring
def characterReplacement(s: str, k: int) -> int:
    max_length=0
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            substring=s[i:j+1]

            freq={}
            for char in substring:
                freq[char]=freq.get(char,0)+1
            
            max_freq=max(freq.values())

            replacements_needed=len(substring)-max_freq

            if replacements_needed<=k:
                max_length=max(max_length,len(substring))
        
    return max_length

print(characterReplacement(s = "ABAB", k = 2))


# Time complexity : O(N)
# Space complexity : O(len(window))
def characterReplacement(s: str, k: int) -> int:
    freq={}
    left=0
    max_length=0

    for right, ch in enumerate(s):
        freq[ch]=freq.get(ch,0)+1

        len_substring=right-left+1

        max_freq=max(freq.values())

        replacements_needed=len_substring-max_freq

        if replacements_needed<=k:
            max_length=max(max_length,len_substring)
        else:
            freq[s[left]]-=1
            left+=1
    
    return max_length

print(characterReplacement(s = "AABABBA", k = 1))
        


    



