class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Approach

        # 1. Brute Force - Nested Loops
        # For each number in nums1, find its position in nums2 and scan for the next greater element.
        # Time complexity : O(N * M), Space complexity : O(1)

        # 2. Optimal Solution - Monotonic Stack + HashMap
        # Use a decreasing stack to find the next greater element efficiently.
        # Time complexity : O(N + M), Space complexity : O(N)
        
        nums1_idx = {n:i for i,n in enumerate(nums1)}

        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]

            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1_idx[val]
                res[idx] = cur
            
            if cur in nums1_idx:
                stack.append(cur)

        return res
