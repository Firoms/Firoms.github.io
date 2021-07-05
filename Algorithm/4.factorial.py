# 팩토리얼 구하기

"""
Input : num = 5

Output : 120
"""


class Solution:
    def factorial(self, num: int):
        def recursion(num):
            if num == 1:
                return 1
            return num * recursion(num - 1)

        op = recursion(num)
        return op


if __name__ == "__main__":
    num = 5

    op = Solution().factorial(num)
    print(op)
