class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        # Approach

    # 1. Brute Force - Try All Subarrays
    # For each start index, expand the window and count the number of zeros.
    # If zeros exceed k, stop expanding.
    # Time complexity : O(N^2), Space complexity : O(1)

    # 2. Optimal Solution - Sliding Window
    # Use two pointers to expand and contract the window.
    # Track the number of zeros, and shrink the window when zero count exceeds k.
    # Time complexity : O(N), Space complexity : O(1)
    
        left = 0      # Left pointer of the window
        zeros = 0     # Count of zeros in the current window
        max_len = 0   # Result: max window size

        for right in range(len(nums)):
            # If current element is 0, increment zero count
            if nums[right] == 0:
                zeros += 1

            # If zeros exceed k, shrink window from the left
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1  # shrink the window

            # Update max_len with the current valid window size
            max_len = max(max_len, right - left + 1)

        return max_len
        
