from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # Approach

    # 1. Brute Force - Try All Swaps (Inefficient)
    # Try all possible frequency rearrangements, too slow.
    # Time complexity : O(N!), Space complexity : O(N)

    # 2. Optimal Solution - Use Counter and Sets
    # - Count frequency of each character in both strings.
    # - Ensure both strings use the same characters.
    # - Ensure the sorted list of frequencies match.
    # Time complexity : O(N log N), Space complexity : O(N)

        if len(word1) != len(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        if set(freq1.keys()) != set(freq2.keys()):
            return False

        return sorted(freq1.values()) == sorted(freq2.values())
        
