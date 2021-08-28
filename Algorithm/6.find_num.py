# 이분탐색

"""
Input : nums = [1, 4, 5, 6, 7, 8, 9, 10]
        1) num = 8
        2) num = 13

Output : 1) 5
        2) -1  (찾지 못한다면 -1)
"""


class Solution:
    def findNum(self, nums: list, num: int):
        endPoint = len(nums) - 1
        startPoint = 0
        while startPoint < endPoint:
            avgIdx = (startPoint + endPoint) // 2
            if num < nums[avgIdx]:
                endPoint = avgIdx - 1
            elif num > nums[avgIdx]:
                startPoint = avgIdx + 1
            else:
                return avgIdx
        return -1


if __name__ == "__main__":
    nums = [1, 4, 5, 6, 7, 8, 9, 10]
    num = 8
    op = Solution().findNum(nums, num)
    print(op)
    num = 13
    op = Solution().findNum(nums, num)
    print(op)
