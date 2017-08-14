class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Regular Expression
        result = []
        
        for word in words:
            if re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match(word):
                result.append(word)
        
        return result

# Approach 2  
# The approach is to create an abject which has different value for letters of each row.
# We then traverse through each word using a for-each loop.
# We then use a for loop and check if all letters of current word fall in the same row.
# If yes, we add current word to our 'result' list else we move to next iteration.
# Finally, we return our 'result' list.
      
# row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
# row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
# row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'] 
# result = []

# for word in words:
#     if len(word) == 0:
#         continue

#     if len(word) == 1:
#         result.append(word)
#         continue

#     i = 0
#     while(i < len(word)-1):
#         i += 1
#         b = (word[i] in row1 and word[i-1] in row1) or (word[i] in row2 and word[i-1] in row2) or (word[i] in row3 and word[i-1] in row3)
#         if not b:
#             break

#         if i == len(word)-1:
#             result.append(word)


# return result
