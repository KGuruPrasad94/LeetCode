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
