class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #Approach 
        # 1. Brute force - Use 3 loops and find all elements that sum up to 0
        #Time complexity : O(n^3), Space complexity : O(1)

        #2. Optimal Solution - Sort the array and use two pointers approach
        #Time complexity : O(n^2) + O(nlogN) => O(n^2), Space complexity : O(1)
        
        res = []
        nums.sort() # sort nums

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # skip duplicate elements
                continue

            l = i+1 # use 2 pointers
            r = len(nums)-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total > 0: # if sum > 0, reduce r pointer
                    r -= 1
                elif total < 0: # if sum > 0, increase l pointer
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1

                    while nums[l] == nums[l-1] and l < r: # handel duplicate triplets
                        l += 1
            
        return res
