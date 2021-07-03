# 동명이인 찾기

"""
Input : names = ["Tom", "Jerry", "Mike", "Tom"]

Output : ["Tom"]
"""

class Solution:
    def find_same_name1(self, names: list):
        import copy
        
        set_names = list(set(names))
        op_names = copy.deepcopy(names)
        for i in set_names:
            op_names.remove(i)
        op_names = list(set(op_names))

        return op_names

    def find_same_name2(self, names: list):
        from collections import defaultdict
        name_dict = defaultdict(int)
        for i in names:
            name_dict[i] += 1
        op_names = []
        for i, j in name_dict.items():
            if j>1:
                op_names.append(i)
        return op_names

if __name__ == "__main__":
    names = ["Tom", "Jerry", "Mike", "Tom"]

    op1 = Solution().find_same_name1(names)
    print(op1)

    op2 = Solution().find_same_name2(names)
    print(op2)