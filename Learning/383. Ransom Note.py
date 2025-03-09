class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # Approach

        # 1. Brute Force - Search each letter in magazine for ransomNote
        # For each letter in ransomNote, scan the magazine to check if it exists.
        # Time complexity : O(NM), Space complexity : O(1)

        # 2. Optimal Solution - HashMap (Dictionary)
        # Count occurrences of letters in magazine, then decrement when using them.
        # Time complexity : O(N + M), Space complexity : O(N)

        ltcount = {}

        for c in magazine:
            ltcount[c] = ltcount.get(c,0) + 1

        for c in ransomNote:
            if c not in ltcount or ltcount[c] == 0:
                return False
            
            ltcount[c] -= 1
        
        return True
