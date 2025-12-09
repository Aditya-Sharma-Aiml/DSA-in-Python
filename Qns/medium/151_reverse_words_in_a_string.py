# 2 Pointer solution
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()

        # Two pointers approach
        left, right = 0, len(s) - 1

        while left < right:
            # Swap the words
            s[left], s[right] = s[right], s[left]
            # Move pointers
            left += 1
            right -= 1

        # Convert the list back to a string
        return ' '.join(s).strip()
    
        # Time Complexity O(n)
        # Space Complexity O(n)
    
# Built-in functions solution
class Solution:
    def reverseWords(self, s: str) -> str:        
        return " ".join(s.split()[::-1])
    
        # Time Complexity O(n)
        # Space Complexity O(n)