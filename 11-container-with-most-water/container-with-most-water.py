class Solution:
    def maxArea(self, height: list[int]) -> int:
        container1 = 0
        container2 = len(height) - 1
        maxWater = 0

        while container1 < container2:
            currWater = (container2 - container1) * (min(height[container1], height[container2]))
            maxWater = max(maxWater, currWater)

            # Always move the pointer pointing to smallest line
            if height[container1] <= height[container2]:
                container1 += 1
            else:
                container2 -= 1
        
        return maxWater