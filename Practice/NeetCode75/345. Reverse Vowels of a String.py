class Solution:
    def reverseVowels(self, s: str) -> str:

        # Approach

    # 1. Brute Force - Store and Replace Vowels
    # Store all vowels in a list during the first pass.
    # During the second pass, replace vowels in the string from the end of the list.
    # Time complexity : O(N), Space complexity : O(N)

    # 2. Optimal Solution - Two Pointers and In-Place Swapping
    # Use two pointers from both ends to find vowels and swap them.
    # Uses a set for O(1) vowel lookup and modifies the list in place.
    # Time complexity : O(N), Space complexity : O(1)

        vowels = set('aeiouAEIOU')
        left = 0
        right = len(s) - 1
        s = list(s)

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)
