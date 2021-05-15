#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        center = 1
        answer = []
        while center < len(nums) - 1:
            left = 0
            right = len(nums) - 1
            while left < center and right > center:
                if nums[left] + nums[center] + nums[right] == 0:
                    answer.append(str(nums[left]) + '/' + str(nums[center]) + "/" + str(nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[center] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
            center += 1

        answer = list(set(answer))
        answer = [a.split("/") for a in answer]
        return answer
# @lc code=end

