class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # Find the meeting point of slow and fast pointers in the cycle
        while True:
            slow = nums[slow]  # Move slow pointer one step
            fast = nums[nums[fast]]  # Move fast pointer two steps
             # If slow and fast meet, a cycle exists (duplicate present)
            if slow == fast:
                break

        # Once a cycle is found, reset slow to the beginning and use another pointer
        slow2 = 0
        while True:
            slow = nums[slow]  # Move slow pointer one step
            slow2 = nums[slow2]  # Move slow2 pointer one step
            # When slow and slow2 meet again, they point to the duplicate
            if slow == slow2:  
                return slow

        # Time Complexity O(n)
        # Space Complexity O(1)
