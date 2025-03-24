class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # Approach

    # 1. Brute Force - Use Three Nested Loops
    # Try every triplet combination and check if nums[i] < nums[j] < nums[k].
    # Time complexity : O(N^3), Space complexity : O(1)

    # 2. Better Approach - Track LIS (Length 3)
    # Use a list to track the increasing subsequence and check if its length reaches 3.
    # Time complexity : O(N), Space complexity : O(N)

    # 3. Optimal Solution - Greedy with Two Pointers
    # Track the smallest and second smallest numbers (num_i, num_j).
    # If we find a third number greater than both, return True.
    # Time complexity : O(N), Space complexity : O(1)

        num_i = num_j = float('inf')

        for n in nums:
            if n <= num_i:
                num_i = n
            elif n <= num_j:
                num_j = n
            else:
                return True

        return False 
