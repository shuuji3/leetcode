class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # In case of non multiple
        if len(nums) % k != 0:
            return False

        sorted_nums = sorted(nums)
        for _ in range(len(nums) // k):
            first_num = sorted_nums[0]
            for i in range(k):
                target_num = first_num + i
                if target_num in sorted_nums:
                    sorted_nums.pop(sorted_nums.index(target_num))
                else:
                    return False
        return True
