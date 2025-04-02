class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        # Approach

    # 1. Brute Force - Loop and Check Membership
    # For each element in nums1, check if it's not in nums2 and vice versa.
    # Use a list to store the result while ensuring uniqueness.
    # Time complexity : O(N * M), Space complexity : O(N + M)

    # 2. Optimal Solution - Use Sets
    # Convert both arrays to sets to remove duplicates and enable set difference operations.
    # Use set1 - set2 to find elements only in nums1.
    # Use set2 - set1 to find elements only in nums2.
    # Time complexity : O(N + M), Space complexity : O(N + M)

        set1 = set(nums1)
        set2 = set(nums2)

        diff1 = list(set1 - set2)

        diff2 = list(set2 - set1)

        return [diff1, diff2]
        
