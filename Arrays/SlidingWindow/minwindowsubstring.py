'''
MINIMUM WINDOW SUBSTRNG

Given 2 strings s and t of lengths m and n respectively. return the minimum window substring of s that every character in t (including duplicates) is included in the window.
If there is no such substring, return " "
'''

'''
APPROACH

- Brute force approach :
1. Initialize an empty char count map, min_string and min_length
2. Iterate over t and build the char count map.
3. Iterate over s - left pointer     (outer)
    - Initialize empty window count map
    - Iterate right pointer from left pointer to end
        - if character is part of char count, add it to window count with updated frequeny
        - Check if character frequency in window count is less that character frequency in char count (ensures, all characters in t are covered)
4. Return min_string

- Sliding window approach : (Idea is have and need keep track of characters, by comparing we know if we have a valid string or not)
1. Initialize an empty char count and window count map, min string and min length
2. Build the char count with t and initialize need to the length of it (i.e unique values for char count)
3. initialize have to 0 and left pointer also to 0 (starting)
4. Iterate over s (right pointer) and add element to window_count:
    - if the element is present in char_count and the frequency is same in both char_count and window_count, then we have that element (have+=1)
    - while have == need (i.e all elements needed are in have (count wise)) otherwise continue the expanding using right pointer
        - calculate the current window length, if lesser than minimum, update min_string and min length
        - now the window is valid and captured, next window by shifting it right i.e remove left-=1
        - Since we've removed that element, we need to check if it affects have so :
            - If ch in char count and frequency of ch < frequency in ch account, have -=1
        if that ch is 0, just delete it (clean up)
        - increment left pointer by 1 (shifting window by 1)
5. Reutrn min_string



'''

# Time complexit : O(N^2) - it's not O(N^3) even those there are 3 loops is because alphabets are bounded by max 26, can consider it to be constant.
# Space complexity : O(26)
def minWindow(s: str, t: str) -> str:
    char_count={}
    min_string=""
    min_length=float('inf')

    for ch in t:
        char_count[ch]=char_count.get(ch,0)+1
    
    for i in range(0,len(s)):
        window_count={}
        for j in range(i,len(s)):
            if s[j] in char_count:
                window_count[s[j]]=window_count.get(s[j],0)+1

            valid=True
            for ch in char_count:
                if window_count.get(ch,0) < char_count[ch]:
                    valid=False
                    break
            
            if valid:
                substring=s[i:j+1]
                if len(substring)<min_length:
                    min_string=substring
                    min_length=len(substring)
    
    return min_string

print(minWindow(s = "ADOBECODEBANC", t = "ABC"))

# Time complexity : O(N)
# Time complexity : O(1)
def minWindow(s: str, t: str) -> str:
    char_count={}
    window_count={}
    
    for ch in t:
        char_count[ch]=char_count.get(ch,0)+1

    need=len(char_count)
    have=0
    left=0
    min_string=""
    min_length=float('inf')

    for right in range(0,len(s)):
        window_count[s[right]]=window_count.get(s[right],0)+1
        if s[right] in char_count and window_count[s[right]]==char_count[s[right]]:
            have+=1 # have is updated only when the frequency of character needed matches frequency of that character in window
        while have==need:
            if (right - left + 1) < min_length:
                min_length = right - left + 1
                min_string = s[left:right+1]

            window_count[s[left]] -= 1
            if s[left] in char_count and window_count[s[left]] < char_count[s[left]]:
                have -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]
            
            left+=1
    
    return min_string


print(minWindow(s = "ADOBECODEBANC", t = "ABC"))

        
        