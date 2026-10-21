class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # sorting first with nums.sort() would take O(nlogn) time which is over the limit

        numSet = set(nums)
        longestLength = 0

        for num in numSet:
            if num - 1 not in numSet:
                currNum = num
                currLength = 1

                while currNum + 1 in numSet:
                    currNum += 1
                    currLength += 1
                
                longestLength = max(longestLength, currLength)
        return longestLength





        