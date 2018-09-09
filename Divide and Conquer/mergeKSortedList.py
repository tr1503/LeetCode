'''Use divide and conquer to merge two linked list and recursive to only one linked list'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwo(self, l1, l2):
        node = ListNode(0)
        t = node
        if l1 is None and l2 is None:
            return None
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                t.next = ListNode(l1.val)
                l1 = l1.next
                t = t.next
            else:
                t.next = ListNode(l2.val)
                l2 = l2.next
                t = t.next
        if l1 is None:
            t.next = l2
        if l2 is None:
            t.next = l1
        return node.next
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        ans = []
        for i in range(0, len(lists), 2):
            if i + 1 >= len(lists):
                ans.append(lists[i])
            else:
                ans.append(self.mergeTwo(lists[i],lists[i+1]))
            
        return self.mergeKLists(ans)
