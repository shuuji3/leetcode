#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (27.92%)
# Total Accepted:    558K
# Total Submissions: 2M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
# Example 2:
#
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Create a new list.
        new_list = []
        i1 = 0
        i2 = 0
        while i1 != len(nums1) or i2 != len(nums2):
            if i1 == len(nums1):
                new_list.append(nums2[i2])
                i2 += 1
            elif i2 == len(nums2):
                new_list.append(nums1[i1])
                i1 += 1
            elif nums1[i1] < nums2[i2]:
                new_list.append(nums1[i1])
                i1 += 1
            else:
                new_list.append(nums2[i2])
                i2 += 1

        # Calculate median.
        total_len = len(nums1) + len(nums2)
        target_index = (total_len - 1) // 2
        if total_len % 2 == 0:
            return float((new_list[target_index] + new_list[target_index + 1]) / 2.0)
        return float(new_list[target_index])
