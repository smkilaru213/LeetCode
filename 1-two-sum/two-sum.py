class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in nums and i != nums.index(pair):
                return [i, nums.index(pair)]