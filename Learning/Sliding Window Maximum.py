class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # approach
        # Brute Force Approach (O(N * K)) - A simple solution is to iterate over all windows and find the maximum in each.
        # time complexity - (O(N * K)), space complexity - (O(1))

        # Optimized Approach Using Monotonic Deque - use a deque (double-ended queue) to maintain indices of useful elements in decreasing order.

        # Optimized Code (O(N) Time, O(K) Space)
        
        result = []

        q = deque()

        # pop smaller values from q
        for idx, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)

        # remove left value which is outside current window

            if idx >= k and nums[idx-k] == q[0]:
                q.popleft()

        # append only after checking all values in current window

            if idx >= k-1:
                result.append(q[0])

        return result
