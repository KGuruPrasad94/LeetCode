class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Approach

        # 1. Brute Force - Sorting Approach
        # Count occurrences of each number, then sort by frequency.
        # Time complexity : O(N log N), Space complexity : O(N)

        # 2. Optimal Solution - Heap (Priority Queue)
        # Use a hash map to count occurrences, then a heap to extract the k most frequent elements.
        # Time complexity : O(N log N), Space complexity : O(N)

        heap = []
        counter = {}

        # count freq of each number
        for n in nums:
            counter[n] = counter.get(n,0) + 1 

        # push elements to heap with -ve freq to simulate max heap. Heap is always min in python
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))

        res = []

        # append only top k elements to heap (no freq)
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res

        
