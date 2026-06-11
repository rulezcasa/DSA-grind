'''
PERUMUTATION STRING

Given two string s1 and s2, return true if s2 contains a permutation of s1, or false
'''

'''
APPROACH

- Brute force approach :
1. Count the frequency of s1 and store it in a map.
2. Iterate across the full string (outer loop) - this will be the left pointer
    - char_count holds global value which will be reused, so temporarily copy for manipulation
    - Inner loop with iterate from the the left pointer to left+len(s1) (The window size)
        - for each character within the window, check if present in map :
            - if present, reduce frequency by 1 
            - If not present, break out of that window (as permutation isnt avaialble)

    - At the end of each window, check if frequency of all characters is 0, (permutation found) and return True
3. If none of the windows have the permutation, just return False

- Sliding window approach
1. Initialize and maintain two maps - one char count and one window count
2. Build for characters and build for the first window of size = len(s1) and
3. The condition to check for each iteration is whether the window count = character count (i.e all characters in the window are same as the characters needed)
4. Iterate from 1 (after first window) to the point where the right pointer wont go out of bounds for the window size (i.e len(s2)-len(s1)+1)
    - For character exiting the window, decrement frequecy and if zero, delete the eleement
    - For character entering the window, incremenet frequency
    - At each step check if window count and char count are same, if yes return True other False
'''


# Time complexity : O(N^2)
# Space complexity : O(1)
def checkInclusion(s1: str, s2: str) -> bool:
    char_count={}
    for ch in s1:
        char_count[ch]=char_count.get(ch,0)+1
    
    for left in range(0,len(s2)):
        char_count_temp=dict(char_count) #If i directly assign it, it's just a shallow copy where both the varibles point to the same map. using dict copies.
        for i in range(left,left+len(s1)):
            if s2[i] in char_count:
                char_count_temp[s2[i]]=char_count_temp[s2[i]]-1
            else:
                break

        if sum(char_count_temp.values()) == 0:
            return True
        
    return False

print(checkInclusion("ab","eidbaooo"))


# Time complexity : O(N)
# Space complexity : O(1)
def checkInclusion(s1: str, s2: str) -> bool:
    char_count={}
    window_count={}

    for ch in s1:
        char_count[ch]=char_count.get(ch,0)+1

    for i in range(0,len(s1)):
        window_count[s2[i]]=window_count.get(s2[i],0)+1
    
    if window_count == char_count:
        return True

    for left in range(1,len(s2) - len(s1) + 1):
        right=left+len(s1)-1

        window_count[s2[left-1]] -= 1
        if window_count[s2[left-1]] == 0:
            del window_count[s2[left-1]]

        window_count[s2[right]]=window_count.get(s2[right],0)+1

        if window_count==char_count:
            return True
    
    return False

print(checkInclusion("ab","eidbaooo"))


    







         