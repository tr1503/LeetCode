# Definition for singly-linked list.
#class ListNode:
     #def __init__(self, x):
         #self.val = x
         #self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        if l1 is None and l2 is None:
            return dummyHead
        head = dummyHead
        SUM = 0
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                num1 = l1.val
            else:
                num1 = 0
            if l2 is not None:
                num2 = l2.val
            else:
                num2 = 0
            SUM = num1 + num2 + carry
            head.next = ListNode(SUM % 10)
            head = head.next
            carry = (int)(SUM / 10)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
       
        if carry != 0:
            head.next = ListNode(carry)
            
        return dummyHead.next
