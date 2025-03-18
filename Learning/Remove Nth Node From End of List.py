# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Approach

    # 1. Brute Force - Use a List
    # Store all nodes in a list and find the (N-1)th node from the end.
    # Modify the next pointer of the previous node to skip the Nth node.
    # Time complexity : O(N), Space complexity : O(N)

    # 2. Optimal Solution - Two Pointers (Fast & Slow)
    # Use two pointers (fast and slow). Move fast pointer N steps ahead.
    # Then move both pointers one step at a time until fast reaches the end.
    # Slow will be at the (N-1)th node from the end.
    # Modify the next pointer of the slow pointer to remove the Nth node.
    # Time complexity : O(N), Space complexity : O(1)

        dummy = ListNode(0, head)
        left = dummy
        right = dummy

        # Move `right` n+1 steps ahead
        for _ in range(n + 1):
            right = right.next

        # Move both pointers until `right` reaches the end
        while right:
            right = right.next
            left = left.next

        # Remove nth node
        left.next = left.next.next

        return dummy.next  # Updated head
        
