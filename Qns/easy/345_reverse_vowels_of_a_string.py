class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, len(s) - 1

        # Create a character list for easier manipulation
        char_list = list(s)

        while left < right:
            # Move left pointer until it finds a vowel
            while left < right and char_list[left] not in vowels:
                left += 1

            # Move right pointer until it finds a vowel or reaches the beginning (exclusive)
            while left < right and char_list[right] not in vowels:
                right -= 1

            # Swap the vowels
            if left < right:
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1

        # Join the character list back into a string
        return ''.join(char_list)
    
        # Time Complexity O(n)
        # Space Complexity O(n)
