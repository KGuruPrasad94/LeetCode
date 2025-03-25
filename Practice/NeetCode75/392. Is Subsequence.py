class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Approach

    # 1. Brute Force - Check Characters in Order
    # For each character in s, search for it in t starting from the beginning.
    # This fails to maintain the order and is inefficient.
    # Time complexity : O(N*M), Space complexity : O(1)

    # 2. Optimal Solution - Two Pointers
    # Use two pointers to iterate through s and t.
    # Move pointer in s only when characters match.
    # If we reach the end of s, it's a subsequence.
    # Time complexity : O(N), Space complexity : O(1)

        i,j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j+= 1

        return i == len(s)
