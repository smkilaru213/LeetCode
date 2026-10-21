class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1

        # sorted(frequencies) sorts the dictionary keys, key=frequencies.get tells Python to sort based on each key's corresponding frequency, reverse=True puts the highest frequencies first.
        sortedFrequencies = sorted(frequencies, key = frequencies.get, reverse = True) 
        return sortedFrequencies[:k]
        