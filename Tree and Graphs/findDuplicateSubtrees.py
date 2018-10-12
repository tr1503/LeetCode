class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        counts = {}
        res = []
        def getId(root):
            if not root:
                return 0
            #Create an unique id for each node in the tree
            key = root.val << 32 | getId(root.left) << 16 | getId(root.right)
            if key not in counts:
                counts[key] = [len(counts) + 1, 1]
            else:
                counts[key][1] += 1
                if counts[key][1] == 2:
                    res.append(root)
            return counts[key][0]
        getId(root)
        return res
