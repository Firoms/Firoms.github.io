# n부터 m까지 합 구하기

"""
Input : n = 1, m = 100

Output : 5050
"""


class Solution:
    def sum1(self, n: int, m: int):
        sum_value = 0

        for i in range(n, m + 1):
            sum_value += i

        return sum_value

    def sum2(self, n: int, m: int):
        sum_value = (m + n) * (m - n + 1) // 2

        return sum_value


if __name__ == "__main__":
    op1 = Solution().sum1(1, 100)
    print(op1)

    op2 = Solution().sum2(1, 100)
    print(op2)
