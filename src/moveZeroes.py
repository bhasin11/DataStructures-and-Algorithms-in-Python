class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # The approach is to traverse through the given array and check
        # if a given value is zero or not. If not, move that value to the
        # current counter value and then increment that counter. In this
        # way, we move all our non-zero values to the left side of the
        # array and also maintain the relative order of the values. Then,
        # we start another iteration starting from the current counter 
        # value and till length of the array. In each iteration, we mark
        # the values as 0.
        counter = 0
        
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[counter] = nums[i]
                counter += 1
        
        for i in range(counter, len(nums)):
            nums[i] = 0
        