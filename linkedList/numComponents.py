# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        s = set(G)
        res = 0
        while head:
            if head.val in s and (not head.next or head.next.val not in s):
                res += 1
            head = head.next
        return res
