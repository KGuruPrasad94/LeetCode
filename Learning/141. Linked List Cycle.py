# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Approach

        # 1. Brute Force - Use a Hash Set
        # Store visited nodes in a set and check for repeats.
        # Time complexity : O(N), Space complexity : O(N)

        # 2. Optimal Solution - Floyd’s Cycle Detection (Tortoise and Hare)
        # Use two pointers (slow and fast) to detect cycle.
        # Time complexity : O(N), Space complexity : O(1)

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
        
