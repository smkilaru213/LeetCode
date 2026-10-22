class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i in range(len(nums)):
            num = nums[i]
            pair = target - num

            if pair in numsDict:
                return [i, numsDict[pair]]
            
            numsDict[num] = i
