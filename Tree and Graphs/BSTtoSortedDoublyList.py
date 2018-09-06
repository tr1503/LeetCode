'''Use in-order to travelsal BST to get an array. 
Transfer this array to doubly linked list. Time is O(n).'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""     
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        lst = []
        def helper(root):
            if root != None:
                helper(root.left)
                lst.append(root.val)
                helper(root.right)
        helper(root)
        if len(lst) == 0:
            return None
        head = Node(lst[0],None,None)
        tail = head
        for i in range(1,len(lst),1):
            tail.right = Node(lst[i], tail, None)
            tail = tail.right
        tail.right = head
        head.left = tail
        return head
