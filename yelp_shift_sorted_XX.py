from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def listToNode(self, vals: list[int]) -> Optional['ListNode']:

        if not vals or vals[0] is None:
            return None

        head = ListNode(vals[0])
        prev = head

        for i in range(1, len(vals)):
            currentNode = ListNode(vals[i])
            prev.next = currentNode
            prev = currentNode

        return head 
     

class Solution:

    def splitShiftedList(self, head: Optional['ListNode']):

        if not head or not head.next:
            return head, None

        curr = head

        while curr.next:
            if curr.val > curr.next.val:
                # Found break point
                break

            curr = curr.next

        if not curr.next:
            # No break found, list is fully sorted
            return head, None

        # First part: head to curr
        # Second part: curr.next to end
        list1 = head
        list2 = curr.next
        curr.next = None  # Break the list

        return list1, list2




head = ListNode().listToNode([4, 5, 1, 2, 3])
print(Solution().splitShiftedList(head))