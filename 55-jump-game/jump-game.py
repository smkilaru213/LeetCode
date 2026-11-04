
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for i in range(len(nums)):
            # If we cannot reach this index, we're stuck
            if i > maxReach:
                return False

            # Update the farthest index we can reach
            maxReach = max(maxReach, i + nums[i])

            # If we can reach the last index, return True
            if maxReach >= len(nums) - 1:
                return True

        return True