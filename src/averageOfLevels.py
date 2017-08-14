# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        output = []
        outer = [root]
        
        while outer:
            size = len(outer)
            total = 0.0
            inner = []
            while outer:
                temp = outer.pop()
                if temp.left:
                    inner.append(temp.left)
                if temp.right:
                    inner.append(temp.right)
                
                total += temp.val
            
            outer.extend(inner)                
            output.append(total/size)
        
        return output
        