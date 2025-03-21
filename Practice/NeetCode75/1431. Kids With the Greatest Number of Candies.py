class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # Approach

    # 1. Brute Force - Compare Each Kid with All Others
    # For each kid, simulate giving them extraCandies and check if they have the most candies by comparing with all others.
    # Time complexity : O(N^2), Space complexity : O(N)

    # 2. Optimal Solution - Precompute Max and Compare Once
    # Find the current maximum number of candies.
    # For each kid, check if candies[i] + extraCandies >= max.
    # Time complexity : O(N), Space complexity : O(N)

        res = []
        mx = max(candies)

        for i in range(len(candies)):

            if candies[i] + extraCandies >= mx:
                res.append(True)
            else:
                res.append(False)
        
        return res
