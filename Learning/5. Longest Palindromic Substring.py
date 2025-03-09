class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Approach

        # 1. Brute Force - Check all substrings
        # Generate all possible substrings and check if they are palindromes.
        # Time complexity : O(N³), Space complexity : O(1)

        # 2. Optimal Solution - Expand Around Center
        # Expand outward from each character and each pair of adjacent characters to find the longest palindrome.
        # Time complexity : O(N²), Space complexity : O(1)

        res = ""
        maxlen = 0

# Iterate over each character in the string
        for i in range(len(s)):
            # Case 1: Expand around a single character (odd-length palindrome)
            l, r = i, i  # Both pointers start at the same position
            while l >= 0 and r < len(s) and s[l] == s[r]:  # Expand outward while characters match
                if r - l + 1 > maxlen:  # Check if the new palindrome is longer
                    maxlen = r - l + 1
                    res = s[l:r+1]  # Update longest palindrome substring
                l -= 1  # Move left pointer left
                r += 1  # Move right pointer right

            # Case 2: Expand around two adjacent characters (even-length palindrome)
            l, r = i, i + 1  # Start with a two-character center
            while l >= 0 and r < len(s) and s[l] == s[r]:  # Expand outward while characters match
                if r - l + 1 > maxlen:  # Check if the new palindrome is longer
                    maxlen = r - l + 1
                    res = s[l:r+1]  # Update longest palindrome substring
                l -= 1  # Move left pointer left
                r += 1  # Move right pointer right

        return res  # Return the longest palindrome found
