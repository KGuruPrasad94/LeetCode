class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        lp = rp = 1
        res = [1]*len(nums)

        # Approach:
        #1. Brute Force - compute the product of all elements except nums[i] using nested loops.
        #Time complexity : O(n^2), Space complexity : O(1)

        #2. Optimal Solution - Pre Compute prefix and suffix product and store them
        #Time complexity : O(n), Space complexity : O(1)

        for i in range(len(nums)): # compute prefix product
            res[i] = lp
            lp *= nums[i]

        for i in range(len(nums),-1,-1): # compute postfix product
            res[i] *= rp
            rp *= nums[i]

        return res

'''
Clarifying Questions

1️⃣ Can the array contain negative numbers? → Yes.
2️⃣ Are there zeroes in the array? → Yes, handle them carefully.
3️⃣ What if there is only one element? → Return [1] (edge case).
4️⃣ Is extra space allowed? → Only O(1) extra space (excluding output array).

'''



        
