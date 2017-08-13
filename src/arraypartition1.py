class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach is to sort the input list and then only add
        # all even indexed numbers as they will always be the 
        # minimum of any two consecutive numbers. Thus, giving
        # a maximuum sum eventually.
        nums.sort()
        i = 0
        sum = 0
        while(i<len(nums)):
            sum += nums[i]
            i += 2
        
        return sum