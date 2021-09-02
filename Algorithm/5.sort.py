# 정렬

"""
Input : nums = [2, 4, 5, 1, 3]

Output : [1, 2, 3, 4, 5]
"""


class Solution:
    def selectSort(self, nums: list):
        # 선택 정렬
        # 리스트에서 최소값을 찾아 앞에다가 둔다.
        # O(n제곱)
        return op

    def mergeSort(self, nums: list):
        # 병합정렬
        length = len(nums)
        for i in range(0, len(nums), length * 2):
            for j in range(i, i + length):
                for k in range(i + length, i + length + length):
                    try:
                        if nums[j] >= nums[k]:
                            nums[j], nums[k] = nums[k], nums[j]
                            print(nums, length)
                    except:
                        pass
        sum = 0
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                sum = sum + 1
        if sum == (len(nums) - 1):
            return nums
        return self.mergeSort(nums, length * 2)


if __name__ == "__main__":
    nums = [2, 4, 5, 1, 3]

    op1 = Solution().selectSort(nums)
    print(op1)
