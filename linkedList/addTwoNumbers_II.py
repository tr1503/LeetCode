# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        sum = 0
        res = ListNode(0)
        while len(s1) != 0 or len(s2) != 0:
            if len(s1) != 0:
                sum += s1[-1]
                s1.pop()
            if len(s2) != 0:
                sum += s2[-1]
                s2.pop()
            res.val = sum % 10
            head = ListNode(sum // 10)
            head.next = res
            res = head
            sum = sum // 10
        if res.val == 0:
            return res.next
        else:
            return res
