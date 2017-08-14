# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # The approach is to check if the root is null or not.
        # If null, we will return 0 as there is no depth for this root.
        # Else, we will call maxDepth() with 'root.left' and 'root.right'.
        # We will save the return values of both the calls.
        # Finally, we will compare both the values and will return 
        # larger value of the two. We will also add '1' to the result
        # before returning, to include the depth of the 'root' element.
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        