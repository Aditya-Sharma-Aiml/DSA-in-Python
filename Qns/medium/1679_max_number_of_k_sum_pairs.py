# First solution: Using hashmap + complement
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        seen = {}  # Hash table to store elements and their frequencies
        count = 0  

        for num in nums:
            complement = k - num  # Calculate the complement needed for a valid pair
            if complement in seen and seen[complement] > 0:
                # Found a valid pair, increment count and frequency of complement
                count += 1
                seen[complement] -= 1
            else:
                # Add current number to hash table (or increment frequency)
                seen[num] = seen.get(num, 0) + 1

        return count

        # Time Complexity O(n)
        # Space Complexity O(n)
    
# Second solution: Using sorting + two pointers
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        # Sorting the Array
        nums.sort()

        # Set the two pointer
        l, r = 0, len(nums) - 1
        count = 0

        # 3 Cases:
        # nums[l] + nums[r] == k => valid solution
        # nums[l] + nums[r] > k => need to decrease r
        # nums[l] + nums[r] < k => need to increase l
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
            
            elif nums[l] + nums[r] > k:
                r -= 1
            
            else:
                l += 1
        
        return count

        # Time Complexity O(nlogn)
        # Space Complexity O(1)