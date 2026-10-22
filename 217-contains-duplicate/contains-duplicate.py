class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numsSet = set(nums)
        if len(numsSet) != len(nums):
            return True
        return False