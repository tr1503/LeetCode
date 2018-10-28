# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = head
        fast = head
        # get the middle of linked list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        last = slow.next
        prev = head
        # reverse the tail half linked list
        while last.next:
            temp = last.next
            last.next = temp.next
            temp.next = slow.next
            slow.next = temp
        while slow.next:
            slow = slow.next
            if prev.val != slow.val:
                return False
            prev = prev.next
        return True
