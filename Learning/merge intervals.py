class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Approach

        #1. Brute Force - Use 2 for loops to compare every all possible intervals
        #Time complexity : O(n^2), Space complexity : O(1)

        #2. Optimal Solution - Sort the intervals, check for overlapping times
        #Time complexity : (O(N log N)), Space complexity : O(1)

        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
            
        
