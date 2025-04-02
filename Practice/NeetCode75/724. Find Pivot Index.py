class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # Approach

    # 1. Brute Force - Sum Left and Right at Each Index
    # For each index, compute left and right subarray sums.
    # If they match, return the index.
    # Time complexity : O(N^2), Space complexity : O(1)

    # 2. Optimal Solution - Use Total Sum and Running Left Sum
    # total - left_sum - nums[i] gives the right sum.
    # If left == right, return pivot index.
    # Time complexity : O(N), Space complexity : O(1)
    
        total = sum(nums)
        lsum = 0

        for i in range(len(nums)):
            if lsum == total - lsum - nums[i]: #rsum = total - left_sum - nums[i]
                return i
            
            lsum += nums[i]

        return -1
