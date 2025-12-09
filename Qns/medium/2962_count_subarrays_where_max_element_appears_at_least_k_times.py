class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums) # Max element
        l = 0 
        res = 0
        count = 0 # N. of max elem

        for r in range(len(nums)):
            
            # If current element is the maximum element, increment count
            if nums[r] == max_element:
                count += 1

            # Shrink the window from the left while the count is atleast k
            while count >= k:
                # If the element at the left pointer is also the maximum element, decrement count
                if nums[l] == max_element:
                    count -= 1

                l += 1
            res += l

        return res

        # Time Complexity O(n)
        # Space Complexity O(1)