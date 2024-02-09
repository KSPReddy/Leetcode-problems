class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)
            if((right-left+1) - max(count.values())> k):
                count[s[left]] -= 1
                left = left+1
            res = max(res,right-left+1)
        return res