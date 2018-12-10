# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Create a new linked list to store every node which is smaller than x
# And then connect to the original linked list after iter original linked list
class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        newDummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        p = newDummy
        while curr.next:
            if curr.next.val < x:
                p.next = curr.next
                p = p.next
                curr.next = curr.next.next
                p.next = None
            else:
                curr = curr.next
        p.next = dummy.next
        return newDummy.next
        
