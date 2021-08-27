# 동명이인 찾기

"""
Input : names = ["Tom", "Jerry", "Mike", "Tom"]

Output : ["Tom"]
"""


class Solution:
    def findSameName1(self, names: list):
        import copy

        setNames = list(set(names))
        opNames = copy.deepcopy(names)
        for i in setNames:
            opNames.remove(i)
        opNames = list(set(opNames))

        return opNames

    def findSameName2(self, names: list):
        from collections import defaultdict

        nameDict = defaultdict(int)
        for i in names:
            nameDict[i] += 1
        opNames = []
        for i, j in nameDict.items():
            if j > 1:
                opNames.append(i)
        return opNames


if __name__ == "__main__":
    names = ["Tom", "Jerry", "Mike", "Tom"]

    op1 = Solution().findSameName1(names)
    print(op1)

    op2 = Solution().findSameName2(names)
    print(op2)
