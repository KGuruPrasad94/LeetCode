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


'''
Clarifying questions:
1️⃣ Can I buy and sell multiple times? → No, only once.
2️⃣ Do I have to sell at a profit? → No, return 0 if no profit is possible.
3️⃣ Can prices be negative? → No, stock prices are always positive.
4️⃣ What if the array has only one price? → Return 0 (no transactions possible).

Followup questions:
1️⃣ What if you can buy and sell multiple times? → Use Greedy Algorithm (Peaks & Valleys) (LeetCode #122).
2️⃣ What if there is a transaction fee? → Modify profit calculation (LeetCode #714).
3️⃣ What if you can only hold k transactions? → Use Dynamic Programming (LeetCode #188).
4️⃣ What if the prices are in a circular array? → Use Kadane’s Algorithm to find max gain.
'''
            
        
