'''
LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS

given a string s, find the length of the longest substring without duplicate characters.
'''

'''
APPROACH
- Brute force : 
1. Initialize a max count variable to keep track max substring length
2. Run an outer loop traversing the string.
3. Run an inner loop from position of outer loop pointer to end of string (tracking substrings) :
    - If character is unique (not present in set), add to set and increment count
    - If character is present in set, break the inner loop (substring breaks) and move to the next starting string (outer loop).

- Optimal :
1. Initialize a max_len, left pointer and charmap (keeping track of index)
2 Iterate over the string :
    - If ch in charmap, then left becomes index of that ch + 1 (Basically, skipping that subsequence where repition occurs)
    - If ch not in charmap, add unique char with index to charmap and update maxlength (right-left+1)
3. Return max length
'''

# Time complexity : O(N^2)
# Space complexity : O(1)
def lengthOfLongestSubstring(s: str) -> int:
    max_len=0
    for i in range(0,len(s)):
        char_set=set()
        for j in range(i,len(s)):
            if s[j] in char_set:
                break
            else:
                length=j-i+1
                char_set.add(s[j])
        max_count=max(max_len,length)
    
    return max_len

print(lengthOfLongestSubstring("abcabcbb"))


#Time complexity : O(N)
#Space complexity : O(N) - due to hashmap
def lengthOfLongestSubstring(s):
    charmap = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        if ch in charmap:
            left = max(left, charmap[ch] + 1)

        charmap[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len


print(lengthOfLongestSubstring("abcabcbb"))

    



    

        