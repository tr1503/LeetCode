# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''Create a dummy node to put 0 at the beginning of linked list.
Set a pointer to iter from dummy until this pointer or pointer's next is null.
If the value of node is same as the value we need to delete, make its next to next.next.
Otherwise, iter normally. Return dummy.next.'''
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        while tail is not None and tail.next is not None:
            if tail.next.val == val:
                tail.next = tail.next.next
            else:
                tail = tail.next
        return dummy.next
