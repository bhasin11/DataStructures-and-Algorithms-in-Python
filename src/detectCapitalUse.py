class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # The approach is to use a simple regular expression and
        # use the match() to search for a match between 
        # word and regular expression.
        if re.compile('[A-Z]+$|[a-z]+$|[A-Z][a-z]+$').match(word):
            return True
        return False
        
        # or
        # return word.isupper() or word.islower() or word.istitle()