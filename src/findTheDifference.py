class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # The approach is to find the ASCII value of each character of both
        # the strings. Add the ASCII values of each character of String 't' 
        # to a temporary variable and subtract the ASCII values of each
        # character of String 's' from the temporary variable. Finally,
        # return the character with ASCII value of the temp variable. 
        s1 = 0
        
        for x in s:
            s1 ^= ord(x)
        
        for x in t:
            s1 ^= ord(x)
        
        return chr(s1)
            
            
# Approach 2    
# def findTheDifference(self, s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: str
#     """
#     s1 = sum([ord(c) for c in s])
#     s2 = sum([ord(c) for c in t])

#     return chr(s2 - s1)
        