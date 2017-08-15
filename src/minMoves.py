class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The approach is to find the minimum value of the array.
        # Then subtract it from all other values. Add each difference 
        # to a variable. Finally, the value of this variable will be
        # minimum moves required.
        miny = sys.maxint
        moves = 0
        for num in nums:
            miny = miny if miny < num else num
        
        for num in nums:
            moves += num - miny
        
        return moves