#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.26%)
# Total Accepted:    1.2M
# Total Submissions: 4.2M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
#
#
#
#
#
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum_len = 0

        for start in range(len(s)):
            current_substring = s[start:]
            previous_characters = set()
            maximum_substring_len = 0

            for c in current_substring:
                if c not in previous_characters:
                    maximum_substring_len += 1
                    previous_characters.add(c)
                else:
                    break

            maximum_len = max(maximum_len, maximum_substring_len)

        return maximum_len
