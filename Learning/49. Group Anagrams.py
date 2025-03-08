class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Approach

        # 1. Brute Force - Compare each word with every other word
        # Use nested loops to check if two words are anagrams by sorting them.
        # Time complexity : O(N² * M log M), Space complexity : O(N)

        # 2. Optimal Solution - Sorting and Hash Map
        # Sort each word to create a unique key and store anagrams in a hash map.
        # Time complexity : O(N * M log M), Space complexity : O(N)

        # 3. Most Optimal Solution - Character Frequency Count (Hash Map)
        # Use a frequency array (size 26) for each word to create a unique key.
        # Time complexity : O(N * M), Space complexity : O(N)

        anagram_map = defaultdict(list)  # dictionary to store groups of anagrams

        for word in strs:
            sorted_word = ''.join(sorted(word))  # sort the word to get a unique key for anagrams
            
            anagram_map[sorted_word].append(word)  # append the word to the corresponding key in the dictionary

        return list(anagram_map.values())  
        
