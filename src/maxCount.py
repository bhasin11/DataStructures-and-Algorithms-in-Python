class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # Find all common items on which the operation was done.
        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])
        
        return m*n
        