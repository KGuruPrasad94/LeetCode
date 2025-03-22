class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # Approach

    # 1. Brute Force - Try Planting One by One
    # Loop through each plot in the flowerbed.
    # If the current plot and its neighbors are empty (or out of bounds), plant a flower and decrease n.
    # Return True if n reaches 0, else return False after checking all positions.
    # Time complexity : O(N), Space complexity : O(1)

    # 2. (No better optimal solution)
    # Since every plot needs to be checked for valid placement, O(N) is the best achievable time.

        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                empty_right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1

            if n <= 0:
                return True
        
        return False        
