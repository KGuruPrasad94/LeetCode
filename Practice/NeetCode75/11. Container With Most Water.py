class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Approach:
        #1. Brute Force - compute the area for all apirs using nested loops.
        #Time complexity : O(n^2), Space complexity : O(1)

        #2. Optimal Solution - use 2 pointers, l =0, r = n-1, compute max area. I HL < HR increase L, else decrease R
        #Time complexity : O(n), Space complexity : O(1)

        l = 0
        r = len(height)
        marea = 0

        while l < r:
            length = r - l - 1
            breadth = min(height[l],height[r-1])

            marea = max(marea, length * breadth)

            if height[l] < height[r-1]:
                l += 1
            else:
                r -= 1
        
        return marea
