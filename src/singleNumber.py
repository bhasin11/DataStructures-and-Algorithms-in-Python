class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # The approach is to XOR all elements of the 'nums' array.
        # with the help of a for loop. It will gradually remove bits 
        # of all elements occuring twice. The result of each iteration
        # is saved in the first element of the array.
        # Finally, we return the first element of the array.
        # Note: If the array length is 0, 'undefined' value will be returned.
        
        temp = 0
        for num in nums:
            temp ^= num
        
        return temp