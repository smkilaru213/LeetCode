class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numsDict = {}
        for i in nums:
            if i not in numsDict:
                numsDict[i] = 1
            else:
                numsDict[i] += 1
                return True
        return False