class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] + asteroid < 0:
                    stack.pop()
                elif stack[-1] + asteroid == 0:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)

        return stack

        # Time Complexity O(n)
        # Space Complexity O(n)