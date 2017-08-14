class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # The approach is to soearate all words, reverse all words
        # and then join to form the desired sentence.
        return ' '.join([ word[::-1] for word in s.split(' ')])
        