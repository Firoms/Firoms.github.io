# 이분탐색

"""
Input : nums = [1, 4, 5, 6, 7, 8, 9, 10]
        1) num = 8
        2) num = 13

Output : 1) 5
        2) -1  (찾지 못한다면 -1)
"""


class Solution:
    def find_num(self, nums: list, num: int):
        end_point = len(nums) - 1
        start_point = 0
        while start_point < end_point:
            avg_idx = (start_point + end_point) // 2
            if num < nums[avg_idx]:
                end_point = avg_idx - 1
            elif num > nums[avg_idx]:
                start_point = avg_idx + 1
            else:
                return avg_idx
        return -1


if __name__ == "__main__":
    nums = [1, 4, 5, 6, 7, 8, 9, 10]
    num = 8
    op = Solution().find_num(nums, num)
    print(op)
    num = 13
    op = Solution().find_num(nums, num)
    print(op)
