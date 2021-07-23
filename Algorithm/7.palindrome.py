# 회문 찾기

"""
Input : 1) text = 'HEGEH'
        2) text = 'HHGGDD'

Output : 1) True
        2) False
"""


class Solution:
    def palindrome(self, text: str):
        text_len = len(text)
        check = -1
        back_c = text_len
        for i in range(text_len // 2 + 1):
            check += 1
            back_c -= 1
            if text[check] != text[back_c]:
                return False

        return True



if __name__ == "__main__":
    text = 'HEGEH'
    op = Solution().palindrome(text)
    print(op)
    text = 'HHGGDD'
    op = Solution().palindrome(text)
    print(op)

