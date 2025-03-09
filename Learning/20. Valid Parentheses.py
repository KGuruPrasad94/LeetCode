class Solution:
    def isValid(self, s: str) -> bool:

        # Approach

        # 1. Brute Force - Remove Valid Pairs Repeatedly
        # Replace valid pairs iteratively until no more replacements can be made.
        # Time complexity : O(N²), Space complexity : O(N)

        # 2. Optimal Solution - Stack Data Structure
        # Use a stack to store opening brackets and validate closing brackets as they appear.
        # Time complexity : O(N), Space complexity : O(N)

        st = []
        mapping = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in mapping.values():
                st.append(char)
            elif char in mapping.keys():
                if not st or mapping[char] != st.pop():
                    return False
        
        return not st
        
        
