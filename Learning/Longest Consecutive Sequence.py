class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Approach:
        #1. Brute Force - compute length for all sequences using nested loops.
        #Time complexity : O(n^2), Space complexity : O(1)

        #2. Optimal Solution - use hash set for optimized O(1) lookups
        #Time complexity : O(n), Space complexity : O(N)

        
        numsSet = set(nums)  # Convert to set for O(1) lookups
        max_length = 0  # Stores the longest consecutive sequence

        for n in numsSet:
            if n - 1 not in numsSet:  # Start new sequence only if `n` is the smallest in its sequence
                current_num = n
                current_length = 1  # Start with length 1
                
                while current_num + 1 in numsSet:  # Extend sequence
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)  # Update max sequence length
        
        return max_length
