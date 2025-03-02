class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Approach:
        #1. Brute Force - check of all elements pairs using nested loops, until we find duplicate.
        #Time complexity : O(n^2), Space complexity : O(1)

        #2. Optimal Solution - Using Floyd's Algorithm
        #Time complexity : O(n), Space complexity : O(1)

        slow = nums[0]
        fast = nums[0]

        while True: #Detect cycle using Floyd's cycle detection
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: # Find meeting point
                break

        slow2 = nums[0] 

        while slow != slow2: #Find entry point of the cycle (duplicate number)
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
