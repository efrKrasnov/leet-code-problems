class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            elif c in ')}]':
                if len(stack):
                    popped = stack.pop()
                    if not (
                        popped == '(' and c == ')' or
                        popped == '{' and c == '}' or
                        popped == '[' and c == ']'
                    ):
                        return False
                else:
                    return False
                
        return len(stack) == 0