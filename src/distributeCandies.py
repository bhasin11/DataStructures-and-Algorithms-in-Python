class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # The approach is to find number of unique candies
        # and then return the lower of unique candies and 
        # half of total number of candies.
        uniqueCandies = len(set(candies))
        
        return uniqueCandies if uniqueCandies < len(candies)/2 else len(candies)/2