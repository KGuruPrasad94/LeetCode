class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numsMap = {}
        comp = 0

        #approach
        # 1. Brute Force -  Use 2 for loops to check every pair and return indexes. 
        #Time complexity : O(n^2), Space complexity : O(1)
        
        # 2. Optimal solution - Use HashMap to store index of unseen numbers. Iterate through nums array and check if complement of num is present in map. If present, return the index
        #Time complexity : O(n), Space complexity : O(n)

        for i,n in enumerate(nums):
            comp = target - n # calculate complement 

            if comp in numsMap: # if comp found in map, return index
                return(numsMap[comp], i)

            numsMap[n] = i # store the index in map

'''
Claryfying questions:
	1.	“Are the numbers sorted?” → No, they are unsorted.
	2.	“Can there be multiple solutions?” → No, return any one valid solution.
	3.	“Can the same element be used twice?” → No, each number is used once.
	4.	“Can there be negative numbers?” → Yes.
	5.	“What should I return if no pair exists?” → Return an empty list [].

 Follow up questions:
1️⃣ What if the input is sorted? → Use Two-Pointer Technique (O(N) time, O(1) space).
2️⃣ What if there are multiple valid answers? → Return any one.
3️⃣ What if the input is very large? → Use streaming algorithms (handling data efficiently).
4️⃣ How to solve this in a functional programming style? (Lambda functions in Python).
5️⃣ Can you solve it using Binary Search? (If sorted, yes).

'''
