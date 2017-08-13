class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # The approach is to XOR 'x' and 'y' first.
        # The result of these two numbers will have bits which were not equal.
        # Eg) Suppose x (in binary) is   0001, and
        #     Suppose y (in binary) is   1100, 
        #     Then XOR of 'x' and 'y' is 1101.
        # We then keep right shifting by 1 and check if the right most bit is 1.
        # If yes, we increment the counter variable by 1.
        # Finally, once the number becomes 0, we return the counter variable.
         
        x = x ^ y
        count = 0
        while(x):
            count += x%2
            x /= 2
        
        return count