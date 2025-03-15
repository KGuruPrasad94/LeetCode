class MinStack:

    # Approach

        # 1. Brute Force - Traverse Stack to Find Min
        # Each time getMin() is called, iterate through the entire stack to find the min.
        # Time complexity : O(N) for getMin(), Space complexity : O(N)

        # 2. Optimal Solution - Use an Auxiliary Min Stack
        # Maintain an extra stack (`minStack`) that stores the minimum value at each step.
        # Time complexity : O(1) for all operations, Space complexity : O(N)

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
