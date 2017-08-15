# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """         
        # The approach is to recursively call the 'invertTree'
        # function and invert the left and right child of the 
        # current root. Finally, return the root.
         
        if not root:
            return

        temp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp
        
        return root
        
        