# 회문 찾기

"""
Input : 1) text = 'HEGEH'
        2) text = 'HHGGDD'

Output : 1) True
        2) False
"""


class Solution:
    def palindrome(self, text: str):
        textLen = len(text)
        check = -1
        backC = textLen
        for i in range(textLen // 2 + 1):
            check += 1
            backC -= 1
            if text[check] != text[backC]:
                return False

        return True


if __name__ == "__main__":
    text = "HEGEH"
    op = Solution().palindrome(text)
    print(op)
    text = "HHGGDD"
    op = Solution().palindrome(text)
    print(op)
