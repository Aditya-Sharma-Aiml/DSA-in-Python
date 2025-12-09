class Solution:
    def compress(self, chars: List[str]) -> int:
        
        length = len(chars)

        if length < 2:
            return length

        anchor = 0
        write = 0

        for pos, char in enumerate(chars):

            if (pos + 1) == length or char != chars[pos+1]:
                chars[write] = char
                write += 1

                if pos > anchor:
                    repeated_times = pos - anchor + 1

                    for num in str(repeated_times):
                        chars[write] = num
                        write += 1

                anchor = pos + 1

        return write

        # Space Complexity O(n)
        # Time Complexity O(1)