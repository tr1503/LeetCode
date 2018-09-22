'''Use two points to get time O(n) and space O(1) method.
We can use one slow pointer and one fast point to check cycle.
If it is cycle, the slow pointer should be same as the fast point one time.
If it is not cycle, fast pointer should get the null first.'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
