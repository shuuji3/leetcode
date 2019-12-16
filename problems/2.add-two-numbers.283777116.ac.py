#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.37%)
# Total Accepted:    1.1M
# Total Submissions: 3.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        sum_list: ListNode = None
        current_list = sum_list

        while True:
            sum_val = l1.val + l2.val + carry
            if sum_val >= 10:
                carry = 1
            else:
                carry = 0
            
            new_list = ListNode(sum_val % 10)
            if current_list is None:
                sum_list = new_list
            else:
                current_list.next = new_list
            current_list = new_list
            
            if l1.next is None and l2.next is None:
                if carry == 1:
                    new_list = ListNode(1)
                    current_list.next = new_list
                    current_list = new_list
                break
            elif l1.next is None:
                l1.val = 0
                l2 = l2.next
            elif l2.next is None:
                l2.val = 0
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next
        
        return sum_list
