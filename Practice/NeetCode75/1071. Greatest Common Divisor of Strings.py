class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # Approach

    # 1. Brute Force - Try All Prefixes
    # Check all possible prefixes of str1 and see if it can divide both str1 and str2 completely.
    # Time complexity : O(N * M), Space complexity : O(1)

    # 2. Optimal Solution (Euclid's algorithm Solution)- Use GCD and String Property
    # If str1 + str2 != str2 + str1, there's no common divisor string.
    # If they are equal, the GCD of the lengths gives us the length of the common base string.
    # Return str1[:gcd(len(str1), len(str2))] as the result.
    # Time complexity : O(N + M), Space complexity : O(1)

        if str1 + str2 != str2 + str1:
            return ""

        gcd_len = gcd(len(str1),len(str2))

        return str1[:gcd_len]
