# 최댓값 찾기

"""
Input : nums = [17, 92, 18, 33, 59, 7, 33, 42]

Output : 92
"""


class Solution:
    def findMax1(self, nums: list):
        maxNum = max(nums)
        return maxNum

    def findMax2(self, nums: list):
        maxNum = nums[0]
        for i in nums:
            maxNum = max(maxNum, i)
        return maxNum

    def findMax3(self, nums: list):
        nums.sort()
        maxNum = nums[-1]
        return maxNum


if __name__ == "__main__":
    nums = [17, 92, 18, 33, 59, 7, 33, 42]

    op1 = Solution().findMax1(nums)
    print(op1)

    op2 = Solution().findMax2(nums)
    print(op2)

    op3 = Solution().findMax3(nums)
    print(op3)
