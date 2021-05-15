#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp = ListNode()
        temp.next = head
        prev = temp

        while True:
            i = 0
            test = prev.next
            while i < k:
                if not test:
                    return temp.next
            i = 0
            while i < k:
                
# @lc code=end

