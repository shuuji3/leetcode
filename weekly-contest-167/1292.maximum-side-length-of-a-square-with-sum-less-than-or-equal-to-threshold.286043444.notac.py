#
# @lc app=leetcode id=1292 lang=python3
#
# [1292] Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#
# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/
#
# algorithms
# Medium (39.22%)
# Total Accepted:    2.9K
# Total Submissions: 7.3K
# Testcase Example:  '[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]\n4'
#
# Given a m x n matrix mat and an integer threshold. Return the maximum
# side-length of a square with a sum less than or equal to threshold or return
# 0 if there is no such square.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as
# shown.
# 
# 
# Example 2:
# 
# 
# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],
# threshold = 1
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
# Output: 3
# 
# 
# Example 4:
# 
# 
# Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]],
# threshold = 40184
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 300
# m == mat.length
# n == mat[i].length
# 0 <= mat[i][j] <= 10000
# 0 <= threshold <= 10^5
# 
#
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        max_size = max(rows, cols)
        max_side_length = 0
        
        for i in reversed(range(max_size)):
            size = i+1
            for start_row in range(rows):
                if start_row + size > rows:
                    break
                for start_col in range(cols):
                    if start_col + size > cols:
                        break
                    sum_of_square = 0
                    for row in range(size):
                        mat_row = mat[start_row + row]
                        for col in range(size):
                            sum_of_square += mat_row[start_col + col]
                    if sum_of_square <= threshold:
                        return size
        return 0
    
