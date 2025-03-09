class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Approach

        # 1. Brute Force - Check all quadruplets
        # Use four nested loops to find all possible quadruplets that sum to the target.
        # Time complexity : O(N⁴), Space complexity : O(N)

        # 2. Optimal Solution - Two Pointers + Sorting
        # Sort the array, use two loops to fix the first two numbers, 
        # then use a two-pointer approach to find the remaining two numbers.
        # Time complexity : O(N³), Space complexity : O(N)

        nums.sort()
        res = []
        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]: # skip duplicates for i
                continue

            for j in range(i + 1, len(nums) - 2):
                if j > i +1 and nums[j] == nums[j - 1]: # skip duplicates for j
                    continue

                left , right = j+1, len(nums) - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # need to skip duplicate values for left and right pointers
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return res
