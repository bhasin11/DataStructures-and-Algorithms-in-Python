class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # The approach is to travrse the given array and
        # check if current value of the array is 1.
        # If yes, we increment the value of 'current'
        # value by 1.
        # Else, we make value of 'current' to 0.
        # For each iteration, we also compare the value of
        # 'max' and 'current', and store the larger value
        # in 'max'.
        # Finally, we return the value of 'max'.
        curr = 0
        maxy = 0
        
        for num in nums:
            if num == 1:
                curr += 1
                maxy = max(maxy, curr)
            else:
                curr = 0
        
        return maxy