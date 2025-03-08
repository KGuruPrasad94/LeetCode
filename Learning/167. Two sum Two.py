class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Approach

        # 1. Brute Force - Nested Loops
        # Check all pairs to see if their sum equals the target.
        # Time complexity : O(N²), Space complexity : O(1)

        # 2. Optimal Solution - Two Pointers
        # Use two pointers (left and right) to find the target sum efficiently.
        # Time complexity : O(N), Space complexity : O(1)
        
        left = 0
        right = len(numbers) - 1
        res = []

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                res.append(left + 1)
                res.append(right + 1)
                break

            if total > target:
                right -= 1
            elif total < target:
                left += 1
      
        return res
            
