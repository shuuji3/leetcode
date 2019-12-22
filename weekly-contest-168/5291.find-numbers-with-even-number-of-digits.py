class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digits_list = map(str, nums)
        return len(list(filter(lambda s: len(s) % 2 == 0, digits_list)))
