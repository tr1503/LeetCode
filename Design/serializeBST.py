# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if root:
                result.append(str(root.val))
                helper(root.left)
                helper(root.right)
            else:
                result.append('#')
        result = []
        helper(root)
        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper():
            c = next(arr)
            if c == '#':
                return None
            newNode = TreeNode(int(c))
            newNode.left = helper()
            newNode.right = helper()
            return newNode
        arr = iter(data)
        return helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))