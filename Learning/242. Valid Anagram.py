class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Approach

        # 1. Brute Force - Sorting Approach
        # Sort both strings and compare them.
        # Time complexity : O(N log N), Space complexity : O(N)

        # 2. Optimal Solution - Hash Map (Frequency Count)
        # Use a hash map to count occurrences of each character and compare.
        # Time complexity : O(N), Space complexity : O(1) (since only 26 letters)

        mp = {}

        if len(s) != len(t): # if strings have unequal length return false
            return False

        for c in s:
            mp[c] = mp.get(c,0) + 1 # count occurences of char's in string s

        for c in t:
            if c not in mp.keys() or mp[c] == 0: # If char doesn't exist or count reaches 0 return false
                return False
            mp[c] -= 1

        return True    
