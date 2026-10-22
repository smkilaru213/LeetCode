class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        numDict = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in numDict:
                numDict[num] = i
            else:
                if abs(i - numDict[num]) <= k:
                    return True
                numDict[num] = i
        return False
