'''
Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters.
'''

'''
APPROACH (right explores and if condition fails, we shrink left to check next window)
1. Initialie an empty char_map to keep track of distinct characters and their frequencies
2. Initialize max_length=0 and left pointer=0
3. Iterate right over the string:
    - add the current ch to char_map or increment frequency if already present
    - now check if length of charmap is greater than k (i.e distinct characters more than k - condition fails). If true
        - Decrement the left pointer element frequency from charmap and if zero, delete fully. (leaving element)
        - Increment left poitner by 1 (shifting window)
    - If condition passes i.e distinct character not more than k
        - max_length is greater of max_length or right-left+1 (window size)
4. Return the max_length finally.
'''

# Time complexity : O(N)
# Space complexity : O(len(char_map))
def maxkchar(s : str, k : int) -> int:
    char_map={}
    max_length=0
    left=0

    
    for right in range(0,len(s)):
        char_map[s[right]]=char_map.get(s[right],0)+1

        if len(char_map)>k:
            char_map[s[left]]-=1 # Decrement the leaving element

            if char_map[s[left]]==0: # If 0, delete it completely (cleanup)
                del char_map[s[left]]
            
            left+=1
            
        else:
            max_length=max(max_length,(right-left+1))

    return max_length

print(maxkchar(s = "abcabcabc", k = 2))


'''
WHY A SINGLE SHRINK (if, not while) IS SUFFICIENT HERE:

- Invariant: before each iteration, the window was already valid (len(char_map) <= k),
  because the previous iteration's shrink (if any) always restored validity before moving on.

- Each iteration, `right` adds exactly ONE new character. So len(char_map) can increase 
  by AT MOST 1 per step -> going from <=k to, worst case, exactly k+1.

- Removing ONE character (the one at `left`) either deletes its entry completely 
  (if its count hits 0) or reduces the count -> guaranteed to bring len(char_map) 
  back down to <=k in that same step.

- So one shrink is always enough. The window is valid again immediately after 
  the `if` block - it is NEVER left invalid going into the next `right` iteration.

- This is a PROBLEM-SPECIFIC guarantee (bounded by "one distinct char added per step, 
'''






