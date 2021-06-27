# 최댓값 찾기

"""
Input : nums = [17, 92, 18, 33, 59, 7, 33, 42]

Output : 92
"""


class Solution:
    def find_max1(self, nums: list):
        max_num = max(nums)
        return max_num

    def find_max2(self, nums: list):
        max_num = nums[0]
        for i in nums:
            max_num = max(max_num, i)
        return max_num

    def find_max3(self, nums: list):
        nums.sort()
        max_num = nums[-1]
        return max_num


if __name__ == "__main__":
    nums = [17, 92, 18, 33, 59, 7, 33, 42]

    op1 = Solution().find_max1(nums)
    print(op1)

    op2 = Solution().find_max2(nums)
    print(op2)

    op3 = Solution().find_max3(nums)
    print(op3)
