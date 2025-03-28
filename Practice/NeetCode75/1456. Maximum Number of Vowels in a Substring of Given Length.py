class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # Approach

    # 1. Brute Force - Count Vowels in All Substrings of Length k
    # Generate all substrings of length k and count vowels in each.
    # Time complexity : O(N * K), Space complexity : O(1)

    # 2. Optimal Solution - Sliding Window
    # Use a sliding window of size k to track the count of vowels.
    # Add new character and remove the oldest one as the window moves.
    # Time complexity : O(N), Space complexity : O(1)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Use a set for O(1) vowel lookup
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Initialize left pointer of the window, current vowel count, and max vowels found
        l = 0
        count = 0
        max_vowels = 0

        for r in range(len(s)):
            if s[r] in vowels:
                count += 1

            if r - l + 1 == k:
                # update max_vowels count
                max_vowels = max(max_vowels, count)

                # check if the character leaving the window is a vowel
                if s[l] in vowels:
                    count -= 1

                l += 1

        return max_vowels
