'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example: height = [0,1,0,2,1,0,1,3,2,1,2,1] → Output: 6
'''
'''
The bars are placed next to each other (no gap in between them). The only gap is when height of bar is 0. Essentially, the problem is asking us to calcualte
water on top the bars.
'''

'''
APPROACH : The idea is to calculate water on top of each block and add it to total
1. Initialize left and right to extremes.
2. Initialize total water to 0 (to which water of each block will be added to calculate total water).
3. Initialize left_max and right_max to -inf.
4. As long as left doesnt cross right (left<right):
    - For left and right, compare it with max_left and max_right, if greater update. 
    - Compute water level as min(left_max,right_max) (water can be held uptill the minimum of the maximum blocks)
    - Now, if max_left<right_max:
        - water at this block is water level - heigh[left] (For every block, water can be held uptill the minimum of the maximum blocks - the current block)
        - Add this to the total water
        - Move left by 1. 
    -  if max_right<left_max:
        - water at this block is water level - height[right] (For every block, water can be held uptill the minimum of the maximum blocks - the current block)
        - Add this to the total water
        - Move right by 1. 
5. Return total water

'''

from typing import List

def trapping_water(height : List[int]) -> int :
    left=0
    right=len(height)-1
    total_water=0
    left_max=float('-inf')
    right_max=float('-inf')
    while left<right:
        if height[left]>left_max:
            left_max=height[left]
        if height[right]>right_max:
            right_max=height[right]
        
        water_level = min(left_max,right_max)
        
        if left_max<right_max:
            current_water=water_level-height[left]
            total_water+=current_water
            left+=1
        
        else:
            current_water=water_level-height[right]
            total_water+=current_water
            right-=1
    
    return total_water
    

print(trapping_water(height = [4, 2, 0, 3, 2, 5]))





        
        

