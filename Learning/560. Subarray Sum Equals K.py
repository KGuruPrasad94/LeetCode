class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # Approach

        # 1. Brute Force - Generate all subarrays and check sum
        # Use two nested loops to check the sum of all subarrays.
        # Time complexity : O(N²), Space complexity : O(1)

        # 2. Optimal Solution - Prefix Sum + HashMap
        # Use a hashmap to track prefix sums and count valid subarrays efficiently.
        # Time complexity : O(N), Space complexity : O(N)

        sub_num = {0:1}
        total = count = 0

        for n in nums:
            total += n # Update running sum
            
            # Check if (total - k) exists in hashmap (indicating a valid subarray)
            if total - k in sub_num:
                count += sub_num[total-k]

            # Update hashmap with the current total sum count
            sub_num[total] = 1 + sub_num.get(total, 0)
        
        return count

        
