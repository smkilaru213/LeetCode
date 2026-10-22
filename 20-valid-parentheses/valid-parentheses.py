class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = []
        for char in s:
            if char in "({[":
                bracketStack.append(char)
            else:
                if len(bracketStack) == 0:
                    return False
                if char == ')' and bracketStack.pop() != '(':
                    return False
                if char == '}' and bracketStack.pop() != '{':
                    return False
                if char == ']' and bracketStack.pop() != '[':
                    return False
        return len(bracketStack) == 0
        