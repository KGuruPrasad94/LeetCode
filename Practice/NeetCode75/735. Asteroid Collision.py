class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # Approach

    # 1. Brute Force - Repeatedly Simulate Collisions
    # Iterate and simulate pairwise collisions, repeat until stable.
    # Time complexity : O(N^2), Space complexity : O(N)

    # 2. Optimal Solution - Stack
    # Iterate through asteroids.
    # Use a stack to track "right-moving" asteroids.
    # When a left-moving asteroid is found, resolve collisions with the stack.
    # Time complexity : O(N), Space complexity : O(N)
    
        stack = []

        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else:
                stack.append(ast)

        return stack
