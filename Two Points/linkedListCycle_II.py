'''Use Floyd's Algorithm to solve this question. Set one slow pointer and one fast pointer firstly.
If fast pointer reaches null, this linked list is not cycle, return None. If slow and fast intersect,
return this intersect node. Set two new pointer, one is head another is the intersect node. 
Track these two nodes, get their intersect node. This intersect node must be extrace of cycle.'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersect(self,head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            #Must check if the next one is intersect node
            if slow == fast:
                return slow
        return None
            
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        intersect = self.getIntersect(head)
        if intersect is None:
            return None
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
