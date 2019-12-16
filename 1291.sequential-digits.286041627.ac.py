#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#
# https://leetcode.com/problems/sequential-digits/description/
#
# algorithms
# Medium (49.83%)
# Total Accepted:    4K
# Total Submissions: 8K
# Testcase Example:  '100\n300'
#
# An integer has sequential digits if and only if each digit in the number is
# one more than the previous digit.
# 
# Return a sorted list of all the integers in the range [low, high] inclusive
# that have sequential digits.
# 
# 
# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
# 
# 
# Constraints:
# 
# 
# 10 <= low <= high <= 10^9
# 
# 
#
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        min_length = len(str(low))
        max_length = len(str(high))
        sequential_digits_list = []

        for length in range(min_length, max_length+1):
            for sequential_digits in self.generate_sequential_digits(length):
                if low <= sequential_digits <= high:
                    sequential_digits_list.append(sequential_digits)
        return sorted(sequential_digits_list)

    def generate_sequential_digits(self, length: int) -> int:
        for start_digit in range(1, 10-length+1):
            sequential_digits = ''
            for i in range(length):
                sequential_digits += str(start_digit + i)
            yield int(sequential_digits)
