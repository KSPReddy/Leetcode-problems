class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = s.split()[::-1]
        lis = []
        for i in string:
            lis.append(i)
        return ' '.join(lis) 