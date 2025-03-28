class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        # Approach

    # 1. Brute Force - Check All Pairs
    # Use nested loops to check all pairs and mark used indices.
    # Time complexity : O(N^2), Space complexity : O(N)

    # 2. Optimal Solution - Two Pointers After Sorting
    # Sort the array. Use two pointers (left, right) to find pairs that sum to k.
    # If nums[l] + nums[r] == k, count it and move both pointers.
    # If the sum is too big, move right pointer; if too small, move left pointer.
    # Time complexity : O(N log N) due to sorting, Space complexity : O(1)

        nums.sort()

        l,r = 0, len(nums) - 1
        cnt = 0

        while l < r:
            if nums[l] + nums[r] == k:
                l += 1
                r -= 1
                cnt += 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
            
        return cnt
