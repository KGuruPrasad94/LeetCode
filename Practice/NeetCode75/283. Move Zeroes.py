class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach

    # 1. Brute Force - Create New List and Copy Back
    # Store all non-zero elements in a new list and then add zeros at the end.
    # Copy the new list back to nums.
    # Time complexity : O(N), Space complexity : O(N)

    # 2. Optimal Solution - Two Pointers (In-Place)
    # Use pointer j to track the position of the next non-zero element.
    # First pass: move non-zero elements to the front.
    # Second pass: fill remaining positions with zeros.
    # Time complexity : O(N), Space complexity : O(1)
    
        j=0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # Fill the rest of the array with 0s
        for k in range(j, len(nums)):
            nums[k] = 0 
