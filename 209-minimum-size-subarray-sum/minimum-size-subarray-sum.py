class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        minLength = 9999999999
        currSum = 0

        for right in range(len(nums)):
            if nums[right] >= target:
                return 1
            
            currSum += nums[right]

            while currSum >= target:
                minLength = min(minLength, right - left + 1)
                currSum -= nums[left]
                left += 1
        
        if minLength == 9999999999:
            return 0
        
        return minLength
