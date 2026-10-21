class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        frequencies = {}

        for word in words:
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1
        sortedWords = sorted(frequencies) # sort alphabetically first
        sortedFrequencies = sorted(sortedWords, key = frequencies.get, reverse = True) # then sort frequencies
        return sortedFrequencies[:k]