class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index1 = 0
        index2 = len(numbers) - 1

        while index1 < index2:
            currSum = numbers[index1] + numbers[index2]
            
            if currSum == target:
                return [index1 + 1, index2 + 1] # We add +1 because this problem asks for 1-indexed array, not 0-indexed
            elif currSum < target:
                index1 += 1
            else:
                index2 -= 1


        