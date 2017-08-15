# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.helper(root, 0)
        return root
        
    def helper(self, root, total):
        if not root:
            return total
        
        rightSum = self.helper(root.right, total)
        root.val += rightSum
        leftSum = self.helper(root.left, root.val)
        
        return leftSum
        
        