#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.43%)
# Total Accepted:    741.4K
# Total Submissions: 2.6M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for substring in self.create_substrings(s):
            if self.is_palindrome(substring):
                return substring
        return ''

    def create_substrings(self, s: str):
        length = len(s)
        for substring_length in range(length, 0, -1):  # [3, 2, 1] if s == 'aba'
            i = 0
            j = substring_length
            while j < length + 1:
                yield s[i:j]
                i += 1
                j += 1

    def is_palindrome(self, substring: str) -> bool:
        center_index = len(substring) // 2
        first_part = substring[:center_index + 1]  # 'abc' for 'abcde'
        last_part = reversed(substring[center_index:])  # 'edc' for 'abcde'
        for c1, c2 in zip(first_part, last_part):
            if c1 != c2:
                return False
        return True
