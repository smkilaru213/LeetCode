class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        # For every word, we'll calculate its sorted key. If the key already exists, append the word to that group. If it doesn't exist, create a new group.
        
        for word in strs:
            key = "".join(sorted(word)) # sorted() returns a list which can't be a dictionary key, so we need to change it into a string with "".join()
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        # return groups - would return a dictionary, so we convert the dict to a list of lists
        return list(groups.values())
