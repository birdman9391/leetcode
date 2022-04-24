class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        
        left, right = 0, n -1
        
        maxWater = min(height[left], height[right]) * (right - left)
        i, j = left, right
        # return maxWater
        while i < j:
            if height[i] < height[j]:
                i += 1
                while i <= j and height[i] <= height[left]:
                    i+= 1
                if i > j:
                    return maxWater
                # height[i] > height[left]
                water = min(height[i], height[j]) * (j - i)
                if water > maxWater:
                    maxWater = water
                    left, right = i, j
            else:
                j -= 1
                while i <= j and height[j] <= height[right]:
                    j-= 1
                if i > j:
                    return maxWater
                # height[i] > height[left]
                water = min(height[i], height[j]) * (j - i)
                # if water != 40: return water
                if water > maxWater:
                    maxWater = water
                    left, right = i, j
        return maxWater
            
                