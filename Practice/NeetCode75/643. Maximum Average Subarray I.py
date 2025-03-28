class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Approach

    # 1. Brute Force - Calculate Each Subarray Sum
    # For every index, calculate the sum of k elements starting from it.
    # Time complexity : O(N * K), Space complexity : O(1)

    # 2. Optimal Solution - Sliding Window
    # Use a running sum of the current window.
    # Slide the window by removing the element going out and adding the new one.
    # Track the maximum sum seen so far and divide by k at the end.
    # Time complexity : O(N), Space complexity : O(1)
    
        # Initial sum of first window
        sm = sum(nums[:k])
        max_sum = sm

        for i in range(k, len(nums)):
            sm = sm + nums[i] - nums[i - k]
            max_sum = max(max_sum, sm)

        return max_sum / k
