class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = ["(","{","["]
        closers = [")", "}","]"]
        pairs = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in openers:
                stack.append(char)
            elif not stack:
                return False
            elif char in closers:
                if stack.pop() == pairs[char]:
                    continue
                else:
                    return False
        return not stack