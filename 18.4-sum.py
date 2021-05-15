#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        farleft = 0
        center = 2
        answer = []
        while farleft < len(nums) - 3:
            center = farleft + 2
            while center < len(nums) - 1:
                left = farleft + 1
                right = len(nums) - 1
                while left < center and right > center:
                    if nums[farleft] + nums[left] + nums[center] + nums[right] == target:
                        answer.append(str(nums[farleft]) + '/' +str(nums[left]) 
                                + '/' + str(nums[center]) + "/" + str(nums[right]))
                        left += 1
                        right -= 1
                    elif nums[farleft] + nums[left] + nums[center] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
                center += 1
            farleft += 1

        answer = list(set(answer))
        answer = [a.split("/") for a in answer]
        return answer
# @lc code=end

