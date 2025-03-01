class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Approach

        #1. Brute Force - Use 2 for loops to compare every element pair and find max profit
        #Time complexity : O(n^2), Space complexity : O(1)

        #2. Optimal Solution - Find min price seen so far as set as buy price. Calculate profit for each day and find max profit through iteration
        #Time complexity : O(n), Space complexity : O(1)


        buy = prices[0] # assign first price to buy
        profit = 0

        for p in prices[1:]: 
            if p < buy:
                buy = min(buy,p) # find min price and set as buy price

            profit = max(profit,p-buy) # find max profit by iterating through the array and calcualting all profits

        return profit
            
        
