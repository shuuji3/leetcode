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
        substrings = sorted(self.create_substrings(s), key=lambda x: len(x), reverse=True)
        for substring in substrings:
            if self.is_palindrome(substring):
                return substring
        return ''

    def create_substrings(self, s: str):
        length = len(s)
        for i in range(length):
            for j in range(i, length):
                yield s[i:j + 1]

    def is_palindrome(self, substring: str) -> bool:
        i = 0
        j = len(substring) - 1
        while i < j:
            if substring[i] != substring[j]:
                return False
            i += 1
            j -= 1
        return True
