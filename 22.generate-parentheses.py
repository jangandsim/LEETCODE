#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.recursiveGenPar(0, n, 2*n)
    def recursiveGenPar(self, k,  n, b):
        if b == 1:
            return [')']
        if n == 0:
            return [')' + x for x in self.recursiveGenPar(k - 1, n, b - 1)]
        if k == 0:
            return ['(' + x for x in self.recursiveGenPar(k + 1, n - 1, b - 1)]
        return [')' + x for x in self.recursiveGenPar(k - 1, n, b - 1)] + ['(' + x for x in self.recursiveGenPar(k + 1, n -1, b - 1)]
# @lc code=end

