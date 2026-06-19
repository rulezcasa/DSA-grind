'''
CONTAINER WITH MOST WATER

You are given an integer array height of length n. There are n vetical lines drawn such that two endpoints of the ith line are (i,0) and (i,height[i])
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
'''

'''
APPROACH
- Brute force :
1. Initialize maxrea to be zero
2. Fix i using outer loop
    - iterate j over the height
        - pull out minimum height (since we can't slant the container, the maximum height will be the miniumum height between i and j)
        - compute area as minheight * (j-i) i.e the width
        - if area is greater than maxarea update
3. Iterate untill end, return the maxarea 

- Two pointer:
1. initialize maxarea to be zero
2. Initialize left pointer and right pointer to extremes
3. As long as left<right 
    - Pull out the minmum height (since we can't slant the container, the maximum height will be the minimum height between left and right)
    - compute area as minheight*(right-left) which is nothing but the width
    - if ara is greater than maxarea update
    - if left wall height < right wall height, the area is limited by the left wall, so fixing the right wall, increment left pointer to see if area can be maximized
    - else if right wall height < left wall height, the area is limited by the right wall, so fixing the left wall, decrement right pointer to see if area can be maximized
4. Repeat and return the maxarea
'''

# Time complexity : O(N)
# Space complexity : O(1)
def maxArea(height: list[int]) -> int:
    maxarea=0
    for i in range(0,len(height)):
        for j in range(1,len(height)):
            minheight=min(height[i],height[j])
            area=minheight*(j-1)
            maxarea=max(area,maxarea)
    return maxarea

print(maxArea(height = [1,1]))

# Time complexity : O(N)
# Space complexity : O(1)
def maxArea(height: list[int]) -> int:
    maxarea=0
    left=0
    right=len(height)-1
    while left<right:
        minheight=min(height[left],height[right])
        area=minheight*(right-left)
        maxarea=max(area,maxarea)

        if height[left] < height[right]: # If left height is lesser than right height then, the area is limited by the left wall.
            left+=1 # Increment to see if a taller wall is possible to maximize area
        else: # If right height is lesser, then its limited by the right wall
            right-=1 # Decrement to see if a taller wall is possible to maximimze area
    
    return maxarea

print(maxArea(height = [1,1]))