class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Approach

        # 1. Brute Force - Nested Loops
        # For each temperature, scan the future days to find the next warmer day.
        # Time complexity : O(N²), Space complexity : O(1)

        # 2. Optimal Solution - Monotonic Decreasing Stack
        # Use a stack to track decreasing temperatures and update results efficiently.
        # Time complexity : O(N), Space complexity : O(N)
        
        res = [0] * len(temperatures)  # Initialize result array with 0s
        stack = []  # Stores (temperature, index)

        for i, t in enumerate(temperatures):
            # Pop stack while current temperature is greater
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = i - stackInd  # Calculate wait days

            stack.append((t, i))  # Push current temperature and index

        return res
