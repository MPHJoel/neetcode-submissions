class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        curve = ("(",")")
        sqig = ("{","}")
        sqr = ("[","]")
        for char in s:
            if char == curve[1]:
                if len(stack) == 0 or stack[-1] != curve[0]:
                    return False
                stack.pop(-1)
            elif char == sqig[1]:
                if len(stack) == 0 or stack[-1] != sqig[0]:
                    return False
                stack.pop(-1)
            elif char == sqr[1]:
                if len(stack) == 0 or stack[-1] != sqr[0]:
                    return False
                stack.pop(-1)
            else:
                stack.append(char)
        if len(stack) > 0:
            return False
        return True