# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Approach

        # 1. Brute Force - Store in an Array & Reverse
        # Convert linked list into an array, reverse it, and rebuild the linked list.
        # Time complexity : O(N), Space complexity : O(N)

        # 2. Optimal Solution - Iterative In-Place Reversal
        # Use two pointers (`prev` and `curr`) to reverse links one by one.
        # Time complexity : O(N), Space complexity : O(1)

        prev, curr = None, head

        while curr:
            temp = curr.next # Store the next node - temp variable to store current node next
            curr.next = prev # Reverse the link - point current node next to null (prev)
            prev = curr # shift prev pointer to current node
            curr = temp # shift current node to next node using temp
        
        return prev
