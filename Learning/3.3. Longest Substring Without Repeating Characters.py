class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Approach

        # 1. Brute Force - Check all substrings for uniqueness
        # Generate all substrings and check for duplicate characters.
        # Time complexity : O(N²), Space complexity : O(N)

        # 2. Optimal Solution - Sliding Window + HashSet
        # Use two pointers (left and right) to expand and contract a window, 
        # keeping track of seen characters in a set to ensure uniqueness.
        # Time complexity : O(N), Space complexity : O(N)

        chars = set()
        left = maxlen = 0

        for right in range(len(s)):
            # If a duplicate character is found, shrink the window from the left
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            
            # Add the new character to the set and update max length
            chars.add(s[right])
            maxlen = max(maxlen,right - left +1)

        return maxlen
