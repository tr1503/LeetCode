'''Use stack to store each node begins from the node m. 
When the node reaches node n, pop the stack until it becomes empty.
And change the values of reverse list to each values in stack.'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        rev = None
        tail = head
        stack = []
        i = 1
        flag = False
        while tail is not None:
            if i == m:
                rev = tail
                flag = True
            elif i == n:
                stack.append(tail.val)
                #Start to reverse
                while stack:
                    rev.val = stack.pop()
                    rev = rev.next
                break
            if flag:
                stack.append(tail.val)
            tail = tail.next
            i += 1
        return head
