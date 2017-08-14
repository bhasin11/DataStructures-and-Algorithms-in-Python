class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c > len(nums)*len(nums[0]):
            return nums
        output = []
        row = 0
        col = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(nums[row][col])
                col += 1
                if col >= len(nums[row]):
                    col = 0
                    row += 1
            output.append(temp)
        
        return output
        