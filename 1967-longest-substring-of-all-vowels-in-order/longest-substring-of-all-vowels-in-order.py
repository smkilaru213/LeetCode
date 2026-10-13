class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ret = 0
        length = 1
        vowelCount = 1

        for i in range(1, len(word)):
            if word[i] < word[i - 1]:
                length = 1
                vowelCount = 1

            else:
                length += 1

                if word[i] != word[i - 1]:
                    vowelCount += 1

            if vowelCount == 5:
                ret = max(ret, length)

        return ret
        