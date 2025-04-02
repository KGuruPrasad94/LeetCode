class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # Approach

    # 1. Brute Force - Count and Compare Frequencies
    # Count the frequency of each element using a dictionary.
    # Then, check for duplicates in the frequency values using nested loops.
    # Time complexity : O(N^2), Space complexity : O(N)

    # 2. Optimal Solution - Hashing and Set
    # Use Counter to count occurrences of elements.
    # Use a set to check if all frequency values are unique.
    # Time complexity : O(N), Space complexity : O(N)
    
        freq_map = {}
        freq_set = set()

        for a in arr:
            freq_map[a] = freq_map.get(a, 0) + 1

        for count in freq_map.values():
            freq_set.add(count)

        if len(freq_map) == len(freq_set):
            return True

        return False
