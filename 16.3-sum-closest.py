#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        center = 1
        answer = 1000000
        while center < len(nums) - 1:
            left = 0
            right = len(nums) - 1
            while left < center and right > center:
                if nums[left] + nums[center] + nums[right] == target:
                    return target
                elif nums[left] + nums[center] + nums[right] < target:
                    if abs(nums[left] + nums[center] + nums[right] - target) < abs(answer - target):
                        answer = nums[left] + nums[center] + nums[right]
                    left += 1
                else:
                    if abs(nums[left] + nums[center] + nums[right] - target) < abs(answer - target):
                        answer = nums[left] + nums[center] + nums[right]
                    right -= 1
            center += 1
        return answer
# @lc code=end

