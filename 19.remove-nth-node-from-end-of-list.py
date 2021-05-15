#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        x = self.recursiveSearch(head, n)
        if x == n:
            head = head.next
        return head
    def recursiveSearch(self, head, n):
        if not head.next:
            return 1
        k = self.recursiveSearch(head.next, n)
        if k == n:
            head.next = head.next.next

        return k + 1
# @lc code=end

