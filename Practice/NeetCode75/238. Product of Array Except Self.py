class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Approach

    # 1. Brute Force - Use Nested Loops
    # For each element, compute product of all other elements.
    # Time complexity : O(N^2), Space complexity : O(1)

    # 2. Optimal Solution - Use Prefix and Suffix Products
    # First pass: calculate product of elements to the left of each index.
    # Second pass: multiply with product of elements to the right.
    # Time complexity : O(N), Space complexity : O(1) (excluding output array)

        lp = rp = 1
        res = [0]*len(nums)

        for i in range(len(nums)):
            res[i] = lp
            lp *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            res[i] *= rp
            rp *= nums[i]

        return res
