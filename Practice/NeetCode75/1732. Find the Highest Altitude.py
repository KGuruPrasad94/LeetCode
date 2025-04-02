class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        psum, mx = 0, 0

        for g in gain:
            psum += g
            mx = max(mx, psum)
        
        return mx
