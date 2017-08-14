class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # The approach is to find the leftmost 1 (in binary) of num.
        # Then create a number which has all 1's till that position of 1.
        # Eg) Suppose num in binary is 1000, 
        #     then we have to make i = 1111.
        # Finally, XOR of num and i will give us complement of num.

        allOnes = 0
        temp = num
        while(temp):
            allOnes *= 2
            allOnes += 1
            temp /= 2
            
        return num ^ allOnes