# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
            
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        temp = node.right
        while temp:
            self.stack.append(temp)
            temp = temp.left

        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())