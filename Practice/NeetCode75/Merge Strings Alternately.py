class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        i,j = 0, 0
        m,n = len(word1), len(word2)
        res = []

        # merge characters alternately
        while i < m and j < n:
            res.append(word1[i])
            res.append(word2[j])

            i += 1
            j += 1
        
        # merge remaining for unequal strings
        res.append(word1[i:])
        res.append(word2[j:])

        return ''.join(res)
