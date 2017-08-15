# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        values = set()
        
        def helper(root):
            if not root:
                return False
            
            if root.val in values:
                return True
            
            values.add(k - root.val)
            return helper(root.left) | helper(root.right)
    
        return helper(root)
        

# Approach 2        
# def findTarget(self, root, k):
#     """
#     :type root: TreeNode
#     :type k: int
#     :rtype: bool
#     """        
#     return self.helper(root, k, [])

# def helper(self, root, target, values):
#     if not root:
#         return False

#     if root.val in values:
#         return True

#     values.append(target - root.val)
#     return self.helper(root.left, target, values) or self.helper(root.right, target, values)
