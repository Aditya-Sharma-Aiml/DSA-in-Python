class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # Keep track of indices of valid parentheses.

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        
        # Stack contains indices of unmatched parentheses.
        # Create a set of these indices for efficient lookup.
        unmatched_indices = set(stack)
        
        # Filter out characters at unmatched indices.
        return ''.join([char for i, char in enumerate(s) if i not in unmatched_indices])

        # Time Complexity O(n)
        # Space Complexity O(n)
