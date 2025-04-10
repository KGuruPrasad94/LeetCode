class Solution:
    def removeStars(self, s: str) -> str:

        # Approach

    # 1. Brute Force - Rebuild String Repeatedly
    # Use a list or string, and scan left-to-right, removing characters each time you hit '*'.
    # Inefficient due to repeated deletion.
    # Time complexity : O(N^2), Space complexity : O(N)

    # 2. Optimal Solution - Stack
    # Iterate through the string. Push normal characters to a stack.
    # On encountering '*', pop from the stack.
    # Join the stack at the end for the result.
    # Time complexity : O(N), Space complexity : O(N)

        stack = []

        for char in s:
            if char == '*':
                if stack:
                    stack.pop()  # Remove the last non-star character
            else:
                stack.append(char)  # Add to the result

        return ''.join(stack)
