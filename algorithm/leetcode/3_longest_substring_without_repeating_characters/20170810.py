class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0
        used_char = {}
        for i in range(len(s)):
            
            # start<=used_char[s[i]]表示的是新出现的
            # 而不是以前用过的
            
            if s[i] in used_char and start <=used_char[s[i]]:
                start = used_char[s[i]]+1
            max_len = max(max_len, i-start+1)
            used_char[s[i]] = i

        return max_len
