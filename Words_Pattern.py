class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words)!=len(pattern):
            return False
        pattern_dict={}
        words_dict={}
        for i in range(len(pattern)):
            if words[i] not in words_dict:
                words_dict[words[i]]=pattern[i]
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]]=words[i]
            if words_dict[words[i]]!=pattern[i] or pattern_dict[pattern[i]]!=words[i]:
                return False
        return True
