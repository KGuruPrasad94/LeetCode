class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Approach

        #1. Brute Force - Use 2 for loops to compare every all possible subarrays and compute their sums
        #Time complexity : O(n^2), Space complexity : O(1)

        #2. Optimal Solution - Use Kadane's algorithm
        #Time complexity : O(n), Space complexity : O(1)

        curr_tot = maxsum = 0

        for n in nums:
            curr_tot += n # compute current running total

            maxsum = max(maxsum,curr_tot) # find max sum seen

            if curr_tot < 0: # if current running total < 0, then set current running total = 0
                curr_tot = 0

        return maxsum


'''
Clarifying Questions
1️⃣ Can the array contain negative numbers? → Yes, both positive and negative numbers are allowed.
2️⃣ Can the array have only one element? → Yes, return that element itself.
3️⃣ Should I return the subarray or just the maximum sum? → Just the sum, unless asked otherwise.
4️⃣ Are there multiple valid subarrays? → Yes, return the sum of any valid max subarray.

Follow-Up Questions

1️⃣ What if the array is circular (wraps around)? → Use Kadane’s Algorithm for Circular Arrays.
2️⃣ What if the array has multiple max subarrays? → Return any valid one.
3️⃣ Can this be solved using Divide & Conquer? → Yes, in O(N log N) time.
4️⃣ Can we optimize it for streaming data (large inputs)? → Yes, use sliding window variations.
'''
                
        
