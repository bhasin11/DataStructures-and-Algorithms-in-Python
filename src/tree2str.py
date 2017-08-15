# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        result = str(t.val)
        
        if left and right:
            result += '(' + left + ')(' + right + ')'
        
        elif left:
            result += '(' + left + ')'
            
        elif right:
            result += '()(' + right + ')'
            
        return result
        