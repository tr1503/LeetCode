# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        if l1 == None and l2 != None:
            return l2
        if l1 != None and l2 == None:
            return l1
        if l1.val <= l2.val:
            node = ListNode(l1.val)
            l1 = l1.next
        else:
            node = ListNode(l2.val)
            l2 = l2.next
        t = node
        while l1 != None or l2 != None:
            if l1 == None:
                t.next = ListNode(l2.val)
                l2 = l2.next
                t = t.next
                continue
            if l2 == None:
                t.next = ListNode(l1.val)
                l1 = l1.next
                t = t.next
                continue
            if l1.val <= l2.val:
                t.next = ListNode(l1.val)
                l1 = l1.next
                t = t.next
            else:
                t.next = ListNode(l2.val)
                l2 = l2.next
                t = t.next
        return node
