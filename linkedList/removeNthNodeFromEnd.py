# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        #Advance the first pointer so that first pointer can have n nodes gap with second node
        for i in range(1,n+2):
            first = first.next
        #Move first node to the end and second node, maintain the gap
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
