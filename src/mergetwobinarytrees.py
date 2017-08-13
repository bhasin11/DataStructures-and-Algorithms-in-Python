# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # The idea is to take a bottom up approach and return the
        # updated/result tree in each call.
        if not t1:
            return t2
        
        if not t2:
            return t1
        temp = TreeNode(t1.val + t2.val)
        temp.left = self.mergeTrees(t1.left, t2.left)
        temp.right = self.mergeTrees(t1.right, t2.right)
        
        return temp
        
        