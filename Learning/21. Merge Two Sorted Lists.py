# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Approach

        # 1. Brute Force - Collect Nodes, Sort, and Rebuild
        # Store all nodes in a list, sort them, and rebuild the linked list.
        # Time complexity : O(N log N), Space complexity : O(N)

        # 2. Optimal Solution - Iterative Merge Using a Dummy Node
        # Use a dummy node to simplify merging two lists in a single pass.
        # Time complexity : O(N), Space complexity : O(1)

        dummy = ListNode()  # Dummy node to simplify edge cases
        temp = dummy  # Temporary pointer to build the merged list

        # Compare nodes from both lists and merge in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next  # Move to the next position
        
        # Attach any remaining elements from either list
        if list1:
            temp.next = list1
        else:
            temp.next = list2

        return dummy.next  # Return the merged list (skipping the dummy node)
