class Solution:
    def compress(self, chars: List[str]) -> int:

        # Approach

    # 1. Brute Force - Use Extra Space
    # Build a new compressed list and copy it back to `chars`.
    # Time complexity : O(N), Space complexity : O(N)

    # 2. Optimal Solution - Two Pointers (In-Place)
    # Use two pointers to count consecutive chars and write compressed results back to the array.
    # Convert count to string and write digits individually.
    # Time complexity : O(N), Space complexity : O(1)

        i, j = 0, 0

        while i < len(chars):
            ch = chars[i]
            cnt = 0

            # count number of repeated chars
            while i < len(chars) and ch == chars[i]:
                i += 1
                cnt += 1

            # write char
            chars[j] = ch
            j += 1

            # write cnt > 1
            if cnt > 1:
                for digit in str(cnt):
                    chars[j] = digit
                    j += 1

        return j
