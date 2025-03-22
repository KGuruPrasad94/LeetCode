class Solution:
    def reverseWords(self, s: str) -> str:

        # Approach

    # 1. Brute Force - Use Stack to Reverse Word Order
    # Split the string into words and push each word into a stack.
    # Pop words from the stack and join them with a space.
    # Time complexity : O(N), Space complexity : O(N)

    # 2. Optimal Solution - Use Two Pointers to Swap Words
    # Split the string by spaces to get words, then use two pointers to reverse the list in-place.
    # Join the reversed list with a single space.
    # Time complexity : O(N), Space complexity : O(1) (excluding space used for output string)

        l = s.split()

        left, right = 0, len(l) - 1

        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

        return ' '.join(l)
