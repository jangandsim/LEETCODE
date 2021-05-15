#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        d = {2 : ['a', 'b', 'c'],
             3 : ['d', 'e', 'f'],
             4 : ['g', 'h', 'i'],
             5 : ['j', 'k', 'l'],
             6 : ['m', 'n', 'o'],
             7 : ['p', 'q', 'r', 's'],
             8 : ['t', 'u', 'v'],
             9 : ['w', 'x', 'y', 'z']
            }
        l = ['']
        while digits:
            n = int(digits[0])
            l = [x + y for x in l for y in d[n]]
            digits = digits[1:]
        
        return l
# @lc code=end

