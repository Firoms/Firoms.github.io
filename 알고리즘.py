from string import ascii_uppercase


def find_num(num, list_):
    last = len(list_) - 1
    first = 0
    while first < last:
        avg = (last + first) // 2
        if num < list_[avg]:
            last = avg - 1
        elif num > list_[avg]:
            first = avg + 1
        else:
            return avg
    return None


def same_str(text):
    text_len = len(text)
    check = -1
    back_c = text_len
    for i in range(text_len // 2 + 1):
        check += 1
        back_c -= 1
        if text[check] != text[back_c]:
            return False

    return True


# 병합 정렬


def bh(li1, length):
    li = li1
    for i in range(0, len(li), length * 2):
        for j in range(i, i + length):
            for k in range(i + length, i + length + length):
                try:
                    if li[j] >= li[k]:
                        li[j], li[k] = li[k], li[j]
                        print(li, length)
                except:
                    pass
    sum = 0
    for i in range(len(li) - 1):
        if li[i] <= li[i + 1]:
            sum = sum + 1
    if sum == (len(li) - 1):
        return li
    return bh(li, length * 2)

    # name = ["Tom", "Jerry","Mike","Tom"]
    # name_set = list(set(name))
    # for i in name_set:
    #     name.remove(i)
    # print(name)


def same_name(name):
    name_list = []
    name_dic = {}
    for i in name:
        if i in name_dic:
            # name_list.append(i)
            name_dic[i] += 1
        else:
            name_dic[i] = 1

    return name_list


def change_list():
    r = [1, 2]
    print(id(r), r)
    r += [3, 4]
    print(id(r), r)

    s = (1, 2)
    print(id(s), s)
    s += (3, 4)
    print(id(s), s)
    """
    change_list()
    """


def add_last(m, n):
    m += n
    print(m)
    """
    r = [1,2]
    add_last(r,[3,4])
    t =(1,3)
    add_last(t,(5,7))
    print(r,t)
    """


def min_max_list(d):
    d.sort()
    print(d[0], d[-1], sep=",")
    """
    I = [3,1,5,4]
    min_max_list(I)
    print(I)
    """


def min_max_tuple(d):
    d = list(d)
    d.sort()
    print(d[0], d[-1], sep=",")
    """
    t = (3,1,5,4)
    min_max_tuple(t)
    print(t)
    """


def find_friend(info, name):
    friend_list = []
    first = info[name]

    def find(names):
        for i in names:
            second = info[i]
            if i not in friend_list:
                friend_list.append(i)
                find(second)

    find(first)
    # friend_list = list(set(friend_list))
    print(friend_list)


"""
fr_info = {
    'Summer':['John', 'Justin', 'Mike'],
    'John':['Summer', 'Justin'],
    'Justin':['John','Summer','Mike','May'],
    'Mike':['Summer', 'Justin'],
    'May':['Justin','Kim'],
    'Kim':['May'],
    'Tom':['Jerry'],
    'Jerry':['Tom'],
}
find_friend(fr_info,'Summer')
"""


def same_is():
    import copy

    # r1 = [1,2,3]
    # r2 = [1,2,3]
    # print(r1 is r2)
    # print(r1==r2)

    r1 = ["John", ("man", "usa"), [175, 23]]
    # r2 = list(r1)
    # r2 = list(r1)
    r2 = copy.deepcopy(r1)
    r2[2][1] += 1
    print(r1, r2)
    print(r1 is r2)
    for i in range(len(r1)):
        print(r1[i] == r2[i])
        print(id(r1[i]), id(r2[i]))


def min_max(li):
    min_num = li[0]
    max_min = 0
    for i in li[1:]:
        if min_num > i:
            min_num = i
        if max_min < i - min_num:
            max_min = i - min_num
    print(max_min)
    """
    min_max([5, 7, 6, 3, 4])
    min_max([5, 3, 6, 7, 4])
    """


def stack_node(ln):
    a = ln
    node_len = 0
    li = []
    while a:
        node_len += 1
        a = a.next
    node_len = node_len // 2
    for i in range(node_len):
        li.append(ln.val)
        ln = ln.next
    if node_len % 2 == 1:
        ln = ln.next
    for i in range(node_len):
        b = li.pop(-1)
        if b != ln.val:
            return False
        ln = ln.next
    return True


"""
ln, ln.next, ln.next.next, ln.next.next.next, ln.next.next.next.next = \
    Node(1), Node(2), Node(3), Node(4), Node(5)
print(stack_node(ln))
"""


class Node:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    """
    ln, ln.next, ln.next.next, ln.next.next.next, ln.next.next.next.next = \
        Node(1), Node(2), Node(3), Node(4), Node(5)
    for i in range(5):
        print(ln.val)
        ln = ln.next
    """
    """
    ln, ln.left, ln.left.left, ln.left.right, ln.right, ln.right.left, ln.right.right = Node(3), Node(9), Node(2), Node(2) ,Node(20), Node(15), Node(7)
    li = []
    li.append(ln)
    length = 0
    while li:
        length+=1
        for _ in range(len(li)):
            a = li.pop(0)
            b = a
            try:
                a = a.left
                li.append(a)
            except:
                pass
            try:
                b = b.right
                li.append(b)
            except:
                pass

    print(length)
    """
    """
    ln1, ln1.right, ln1.right.right = Node(2), Node(4), Node(3)
    ln2, ln2.right, ln2.right.right = Node(5), Node(6), Node(4)
    li = []
    lastcarry = 0
    root = Node(0)
    current = root
    while ln1 and ln2:
        lnsum = ln1.val + ln2.val
        # carry = lnsum//10
        # lnlast = lnsum%10
        carry, lnlast = divmod(lnsum, 10)
        current.right = Node(lnlast+lastcarry)
        current = current.right
        li.append(lnlast+lastcarry)
        ln1 = ln1.right
        ln2 = ln2.right
        lastcarry = carry
    print(li)
    print(root.right.val, root.right.right.val, root.right.right.right.val)
    """


def gen_num():
    print("first number")
    yield 1
    print("second number")
    yield 2
    print("third number")
    yield 3
    """
    # gen_num()
    # print(type(gen_num()))
    gen = gen_num()
    next(gen)
    next(gen)
    next(gen)
    """


def nodebh(ln1, ln2):
    a = ln1
    b = ln2
    renode = Node(0)
    addnode = renode
    while a and b:
        if a.val > b.val:
            addnode.right = Node(b.val)
            addnode = addnode.right
            b = b.right
        else:
            addnode.right = Node(a.val)
            addnode = addnode.right
            a = a.right
    while a:
        addnode.right = Node(a.val)
        addnode = addnode.right
        a = a.right
    while b:
        addnode.right = Node(b.val)
        addnode = addnode.right
        b = b.right
    return renode.right


"""
ln1, ln1.right, ln1.right.right = Node(1), Node(2), Node(4)
ln2, ln2.right, ln2.right.right = Node(1), Node(3), Node(4)
renode = nodebh(ln1, ln2)
print(renode.val, renode.right.val,renode.right.right.val,renode.right.right.right.val,renode.right.right.right.right.val,renode.right.right.right.right.right.val)
"""


def nodedeverse(ln):
    a = ln

    prev = a
    curr = a.right
    next = a.right.right
    curr.right = prev
    prev.right = None

    while next.right:
        prev, curr, next = curr, next, next.right
        curr.right = prev

    next.right = curr
    return next


"""
ln, ln.right, ln.right.right, ln.right.right.right, ln.right.right.right.right = Node(1), Node(2), Node(3), Node(4), Node(5)
a = nodedeverse(ln)
while a:
    print(a.val)
    a = a.right
"""


def find_J(J, S):
    J_li = {}
    for i in J:
        J_li.append(i)
    cnt = 0
    for i in S:
        if i in J_li:
            cnt += 1
    print(cnt)


def nosame(inp):
    maxlen = 0
    for i in range(len(inp)):
        maxpra = 0
        check_li = []
        for j in range(i, len(inp)):
            if inp[j] not in check_li:
                check_li.append(inp[j])
                maxpra += 1
                if maxlen < maxpra:
                    maxlen = maxpra
                continue
            break
    print(maxlen)


def island(land):
    def checkupdownleftright(x, y):
        if x <= -1 or x >= len(land[0]) or y <= -1 or y >= len(land):
            return
        if land[y][x] == "1":
            land[y][x] = "0"
        else:
            return

        checkupdownleftright(x - 1, y)
        checkupdownleftright(x + 1, y)
        checkupdownleftright(x, y - 1)
        checkupdownleftright(x, y + 1)

    islandnum = 0
    # print(land)
    for rownum in range(len(land)):
        for onelandnum in range(len(land[rownum])):
            if land[rownum][onelandnum] == "1":
                islandnum += 1
                checkupdownleftright(onelandnum, rownum)
                # print(land)
    print(islandnum)


"""
island([['1','1','1','1','0','0'],
        ['1','1','0','1','0','1'],
        ['1','1','0','0','1','0'],
        ['0','0','0','1','1','0']])
"""


def sum3(num_li):
    result_li = []
    for a in range(len(num_li)):
        for b in range(a + 1, len(num_li)):
            for c in range(b + 1, len(num_li)):
                if num_li[a] + num_li[b] + num_li[c] == 0:
                    if sorted([num_li[a], num_li[b], num_li[c]]) not in result_li:
                        result_li.append(sorted([num_li[a], num_li[b], num_li[c]]))
    return result_li

    print(sum3([-1, 0, 1, 2, -1, -4]))


def func1(*args):
    print(args)
    # func1()
    # func1(1)
    # func1(1,2)
    # func1(1,2,3)


def func2(**args):
    print(args)
    # func2()
    # func2(a=1)
    # func2(a=1,b=2)
    # func2(a=1,b=2,c=3)


def func3(a, b, c):
    print(a, b, c, sep=",")
    # func3(*[1,2,3])
    # func3(*(0.1,0.2,0.3))
    # func3(*'abc')
    # print("////////////")
    # d = dict(a=1,b=2,c=3)
    # func3(*d)
    # func3(**d)


def group_anagram(li):
    output_list = []
    alp_word_list = []
    for word in li:
        alp_list = []
        for alp in word:
            alp_list.append(alp)
        alp_list.sort()
        alp_word_list.append(alp_list)
    in_list = []
    for i in range(len(li)):
        if i in in_list:
            continue
        match_list = []
        first_list = alp_word_list[i]
        match_list.append(li[i])
        in_list.append(i)
        for j in range(i, len(li)):
            if j in in_list:
                continue
            if first_list == alp_word_list[j]:
                match_list.append(li[j])
                in_list.append(j)
        output_list.append(match_list)
    print(output_list)
    """
    li = ["eat","tea","tan","ate","nat","bat"]
    group_anagram(li)
    """


def warm_day(input_li):
    return_li = []
    for i in range(len(input_li)):
        no_warm = True
        for j in range(i, len(input_li)):
            if input_li[i] < input_li[j]:
                return_li.append(j - i)
                no_warm = False
                break
        if no_warm == True:
            return_li.append(0)
    print(return_li)
    # li = [73,74,75,71,69,72,76,73]
    # warm_day(li)


class Node:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class Far_same:
    def __init__(self, ln):
        self.ln = ln
        self.max_long = 0
        last_long = self.preorder(ln)
        if self.max_long < last_long:
            self.max_long = last_long

    def preorder(self, node):
        cnt = 0
        if node.left != None:
            left_count = self.preorder(node.left)
            if node.val == node.left.val:
                cnt += 1
        else:
            left_count = 0

        if node.right != None:
            right_count = self.preorder(node.right)
            if node.val == node.right.val:
                cnt += 1
        else:
            right_count = 0

        if cnt == 0:
            if self.max_long < left_count + right_count:
                self.max_long = left_count + right_count
            return 0
        elif cnt == 2:
            if self.max_long < left_count + right_count:
                self.max_long = left_count + right_count
            if left_count < right_count:
                return right_count
            else:
                return left_count
        else:
            return cnt + left_count + right_count

    """
    ln, ln.right, ln.right.right = Node(2), Node(5), Node(5)
    ln.left, ln.left.left, ln.left.right, ln.left.left.left = Node(2), Node(2), Node(2), Node(2)
    result = Far_same(ln)
    print(result.max_long)
    """


def dictionary():
    from collections import defaultdict

    s = "robbot"
    # alp_dic = {}
    alp_dic = defaultdict(int)
    for alp in s:
        alp_dic[alp] += 1
        """
        # 1
        if alp in alp_dic:
            alp_dic[alp]+=1
        else:
            alp_dic[alp]=1
        """
        """
        #2
        alp_dic[alp] = alp_dic.setdefault(alp,0) + 1
        """
    print(alp_dic)


def special_method():
    t = (1, 2, 3)
    print(len(t), t.__len__())

    itr1 = iter(t)
    itr2 = t.__iter__()
    for i in itr1:
        print(i, end="")
    for i in itr2:
        print(i, end="")

    print()

    s1 = str(t)
    s2 = t.__str__()
    print(s1, s2)


class Car:
    def __init__(self, id):
        self.id = id

    def __len__(self):
        return len(self.id)

    def __str__(self):
        return "Car num:" + self.id

    def __iter__(self):
        return iter(self.id)

    """
    c = Car("77가 1244")
    print(len(c))
    print(str(c))
    print(c)
    for i in c:
        print(i, end='')
    """


def reverse_list(li):
    rev_li = []
    for i in range(len(li)):
        rev_li.append(li.pop())
    return rev_li
    """
    print(reverse_list(["h","e","l","l","o"]))
    """


class Long_route:
    def __init__(self, ln):
        self.ln = ln
        self.max_long = 0
        last_long = self.preorder(ln)
        self.max_long = str(max(self.max_long, last_long))

    def preorder(self, node):
        if node.left != None:
            left_count = self.preorder(node.left)
            left_count += 1
        else:
            left_count = 0

        if node.right != None:
            right_count = self.preorder(node.right)
            right_count += 1
        else:
            right_count = 0

        self.max_long = max(self.max_long, left_count + right_count)
        return max(left_count, right_count)

    def __str__(self):
        return self.max_long

    """
    ln, ln.right = Node(1), Node(3)
    ln.left, ln.left.left, ln.left.right= Node(2), Node(2), Node(2)
    result = Long_route(ln)
    print(result)
    """


class Min_road:
    def __init__(self, main_road):
        self.main_road = main_road
        self.max_y = len(self.main_road)
        self.max_x = len(self.main_road[0])
        self.first_right()
        self.first_down()
        self.middle_check()

    def first_right(self):
        for i in range(1, self.max_x):
            self.main_road[0][i] += self.main_road[0][i - 1]

    def first_down(self):
        for i in range(1, self.max_y):
            self.main_road[i][0] += self.main_road[i - 1][0]

    def middle_check(self):
        for i in range(1, self.max_y):
            for j in range(1, self.max_x):
                self.main_road[i][j] += min(
                    self.main_road[i - 1][j], self.main_road[i][j - 1]
                )

    def __str__(self):
        return str(self.main_road[-1][-1])

    """
    li = [[1,3,1],[1,5,1],[4,2,1]]
    road = Min_road(li)
    print(road)
    """


def jump_game(li):
    goal = len(li) - 1
    cur = 0
    while goal >= cur:
        jump = li[cur]
        if jump == 0 or cur == goal:
            break
        cur += jump
    if goal == cur:
        return True
    else:
        return False

    """
    print(jump_game([2,3,1,1,4]))
    print(jump_game([3,2,1,0,4]))
    """


def excel(num):
    alp_list = list(ascii_uppercase)
    excel_num = num // 702
    if num % 702 != 0:
        excel_num += 1
    excel_alp = num % 702
    if 0 < excel_alp < 27:
        print(str(excel_num) + str(alp_list[excel_alp - 1]))
    else:
        two_alp = excel_alp - 26
        first_alp = two_alp // 26
        second_alp = two_alp % 26
        if second_alp == 0:
            second_alp = 26
        print(str(excel_num) + str(alp_list[first_alp]) + str(alp_list[second_alp - 1]))
    """
    excel(int(input()))
    """


def alp_print(str_input):
    alp_list = list(ascii_uppercase)
    print_sum = 0
    str_input = "A" + str_input
    for i in range(len(str_input) - 1):
        first = alp_list.index(str_input[i])
        last = alp_list.index(str_input[i + 1])
        if first > last:
            print_sum += min(first - last, 26 - first + last)
        else:
            print_sum += min(last - first, 26 - last + first)
    print(print_sum)
    """
    alp_print('VGXGPUAMKX')
    """


class Node:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class Plustree:
    def __init__(self, ln1, ln2):
        self.result_tree = Node(ln1.val + ln2.val)
        ln1L = ln1.left
        ln1R = ln1.right
        if ln1L == None:
            ln1L = Node(0)
        if ln1R == None:
            ln1R = Node(0)
        ln2L = ln2.left
        ln2R = ln2.right
        if ln2L == None:
            ln2L = Node(0)
        if ln2R == None:
            ln2R = Node(0)
        self.go_left(ln1L, ln2L, self.result_tree)
        self.go_right(ln1R, ln2R, self.result_tree)

    def go_left(self, firstln, secondln, tree):
        tree.left = Node(firstln.val + secondln.val)
        ln1L = firstln.left
        ln1R = firstln.right
        if ln1L == None:
            ln1L = Node(0)
        if ln1R == None:
            ln1R = Node(0)
        ln2L = secondln.left
        ln2R = secondln.right
        if ln2L == None:
            ln2L = Node(0)
        if ln2R == None:
            ln2R = Node(0)

        if ln1L.val != 0 or ln2L.val != 0:
            self.go_left(ln1L, ln2L, tree.left)

        if ln1R.val != 0 or ln2R.val != 0:
            self.go_right(ln1R, ln2R, tree.left)

    def go_right(self, firstln, secondln, tree):
        tree.right = Node(firstln.val + secondln.val)
        ln1L = firstln.left
        ln1R = firstln.right
        if ln1L == None:
            ln1L = Node(0)
        if ln1R == None:
            ln1R = Node(0)
        ln2L = secondln.left
        ln2R = secondln.right
        if ln2L == None:
            ln2L = Node(0)
        if ln2R == None:
            ln2R = Node(0)
        if ln1L.val or ln2L.val != 0:
            self.go_left(ln1L, ln2L, tree.right)
        if ln1R.val or ln2R.val != 0:
            self.go_right(ln1R, ln2R, tree.right)

    def result(self):
        return self.result_tree

    """
    ln1, ln1.right = Node(1), Node(2)
    ln1.left, ln1.left.left = Node(3), Node(1)

    ln2, ln2.left, ln2.right = Node(2), Node(1), Node(3)
    ln2.left.right, ln2.right.right= Node(4), Node(7)

    tree = Plustree(ln1, ln2)
    result = tree.result()

    #                    3
    #               4         5
    #            1    4          7

    print(result.val, result.left.val, result.right.val)
    print(result.left.left.val, result.left.right.val, result.right.right.val)
    """


def turn_pic(pic_li):
    line = len(pic_li[0])
    pic_li.reverse()
    turn_pic_li = []
    for i in range(line):
        one_pic_li = []
        for j in range(line):
            one_pic_li.append(pic_li[j][i])
        turn_pic_li.append(one_pic_li)
    return turn_pic_li
    """
    print(turn_pic([[1,2,3],[4,5,6],[7,8,9]]))
    """


def stoqu(sto_li):
    for i in sto_li:
        for j in range(1, 10):
            if i.count(j) > 1:
                return False

    turn_sto_li = []
    for i in range(9):
        one_sto_li = []
        for j in range(9):
            one_sto_li.append(sto_li[j][i])
        turn_sto_li.append(one_sto_li)

    for i in turn_sto_li:
        for j in range(1, 10):
            if i.count(j) > 1:
                return False

    for l in range(3):
        for _ in range(3):
            box_li = []
            for i in range(3):
                for j in range(3):
                    box_li.append(turn_sto_li[i].pop(0))
                for k in range(1, 10):
                    if box_li.count(j) > 1:
                        return False
        for _ in range(3):
            turn_sto_li.pop(0)
    return True

    """
    print(stoqu([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]))
    """


def sun(num_li):
    result_li = []

    def add_sun(li, test_li):
        # print(li, test_li)
        for i in range(len(test_li)):
            sun_li = list(li)
            add_li = list(test_li)
            if len(add_li) != 0:
                sun_li.append(add_li.pop(i))
                add_sun(sun_li, add_li)

        if len(test_li) == 0 and li != None:
            result_li.append(li)

    for i in range(len(num_li)):
        add_li = list(num_li)
        li = [add_li.pop(i)]
        add_sun(li, add_li)
    # add_sun([1],[2,3])
    print(result_li, len(result_li))
    """
    sun([1, 2, 3, 4, 5, 6, 7, 8, 9])
    """


def network_delay(times, n, k):
    from collections import defaultdict
    import copy

    node_dic = defaultdict(list)
    for node in times:
        node_dic[node[0]].append([node[1], node[2]])
        # node_dic[node[1]].append([node[0], node[2]])
    delay_dic = {k: 0}

    def check_delay(num, node):
        if num not in node:
            return
        elif node[num] == []:
            return
        for j in range(len(node[num])):
            i = node[num][j]
            if i[0] != k:
                give_dic = copy.deepcopy(node)
                if i[0] in delay_dic:
                    delay_dic[i[0]] = min(delay_dic[i[0]], i[1] + delay_dic[num])
                else:
                    delay_dic[i[0]] = i[1] + delay_dic[num]
                give_dic[num].remove(i)
                check_delay(i[0], give_dic)

    check_delay(k, node_dic)
    # print(max(delay_dic.values()))
    if len(delay_dic) == n:
        return max(delay_dic.values())
    else:
        return -1

    """
    result = network_delay([[2,1,1], [2,3,1], [3,4,1]], 4, 2)
    print(result)
    """
    # heapq 모듈을 이용해보자


def plane_mon(times, n, src, dst, k):
    from collections import defaultdict
    import heapq

    node_dic = defaultdict(list)
    for node in times:
        node_dic[node[0]].append([node[1], node[2]])
    cur = [(0, 0, src)]
    money = {}
    while cur:
        time, mon, node = heapq.heappop(cur)
        if time > k + 1:
            break
        if node in money:
            money[node] = min(mon, money[node])
        else:
            money[node] = mon
        for plane in node_dic[node]:
            heapq.heappush(cur, (time + 1, mon + plane[1], plane[0]))
    if dst in money:
        return money[dst]
    return -1
    """
    result = plane_mon([[0, 1, 100], [1, 2, 100], [0, 2, 500]], 3, 0, 2, 0)
    print(result)
    """


def phone_str(num):
    phone_dic = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x" "y", "z"],
    }
    output = []

    def make_str(num, cur):
        if len(num) == 0:
            output.append(cur)
            return
        for i in phone_dic[num[0]]:
            make_str(num[1:], cur + i)

    make_str(num, "")
    return output

    """
    print(phone_str("234"))
    """


def get_kbig(nums, k):
    import heapq

    hq = []
    for i in nums:
        heapq.heappush(hq, -i)
    for _ in range(k):
        num = heapq.heappop(hq)
    print(-num)
    # heapq는 최솟값부터
    """
    get_kbig([3, 2, 3, 1, 2, 4, 5, 5, 6], 2)
    """


class Node:
    def __init__(self, val=0, right=None):
        self.val = val
        self.right = right


def linked_list_sum(li_list):
    fin = 0
    search_li = []
    for i in range(len(li_list)):
        search_li.append(li_list[i].val)
        if li_list[i].right:
            li_list[i] = li_list[i].right

    next_num = min(search_li)
    node = Node(next_num)
    node_add = node
    index_num = search_li.index(next_num)
    search_li.pop(index_num)
    if li_list[index_num]:
        search_li.insert(index_num, li_list[index_num].val)
        li_list[index_num] = li_list[index_num].right
    else:
        fin += 1
        search_li.insert(index_num, None)

    while fin < len(li_list):
        min_li = []
        for i in search_li:
            if i:
                min_li.append(i)
        next_num = min(min_li)
        index_num = search_li.index(next_num)
        node_add.right = Node(search_li.pop(index_num))
        node_add = node_add.right
        if li_list[index_num]:
            search_li.insert(index_num, li_list[index_num].val)
            li_list[index_num] = li_list[index_num].right
        else:
            fin += 1
            search_li.insert(index_num, None)
    return node

    """
    li1, li1.right, li1.right.right = Node(1), Node(4), Node(5)
    li2, li2.right, li2.right.right = Node(1), Node(3), Node(4)
    li3, li3.right = Node(2), Node(6)
    node = linked_list_sum([li1, li2, li3])
    print(node.val, node.right.val, node.right.right.val, node.right.right.right.val, node.right.right.right.right.val, \
        node.right.right.right.right.right.val, node.right.right.right.right.right.right.val,\
        node.right.right.right.right.right.right.right.val, \
        node.right.right.right.right.right.right.right.right)
    """


class Node:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def tree_reverse(node):
    rev_node = node

    def go_down(rev_node):
        if rev_node.left or rev_node.right:
            rev_node.left, rev_node.right = rev_node.right, rev_node.left
        if rev_node.left:
            go_down(rev_node.left)
        if rev_node.right:
            go_down(rev_node.right)

    go_down(rev_node)
    return node

    """
    ln, ln.left, ln.left.left, ln.left.right = Node(4), Node(2), Node(1), Node(3)
    ln.right, ln.right.left, ln.right.right = Node(7), Node(5), Node(4)
    result = tree_reverse(ln)
    def go_down(rev_node):
        print(rev_node.val)
        if rev_node.left:
            go_down(rev_node.left)
        if rev_node.right:
            go_down(rev_node.right)
    go_down(result)
    """


def make_target(candidates, target):
    import copy

    cur_li = []
    suc_li = []
    for i in candidates:
        if i < target:
            cur_li.append([i])
        elif i == target:
            suc_li.append([i])
    while cur_li:
        li = cur_li.pop(0)
        for i in candidates:
            if li[-1] > i:
                continue
            new_li = copy.deepcopy(li)
            new_li.append(i)
            if sum(new_li) == target:
                suc_li.append(new_li)
            elif sum(new_li) <= target:
                cur_li.append(new_li)
    print(suc_li)
    """
    make_target([2,3,6,7], 10)
    """


def get_line(locations, start):
    from collections import defaultdict

    loc_dic = defaultdict(list)
    for i in locations:
        loc_dic[i[0]] += [i[1]]
        loc_dic[i[0]].sort()
    result = [start]
    while loc_dic[result[-1]]:
        cur = loc_dic[result[-1]].pop(0)
        result.append(cur)
    print(result)
    """
    get_line([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], "JFK")
    """


def smallest_num(num_li):
    num = 1
    while True:
        if num not in num_li:
            return num
        num += 1

    """
    print(smallest_num([1, 2, 0]))
    print(smallest_num([3, 4, -1, 1]))
    print(smallest_num([7, 8, 9, 11, 12]))
    """


def make_braket(n):
    braket_li = []

    def make(braket, cur, leftn):
        if leftn > 0:
            make(braket + "(", cur + 1, leftn - 1)
        if leftn == 0:
            braket_li.append(braket + (")" * cur))
        if cur > 0:
            for i in range(cur):
                make(braket + (")" * (i + 1)), cur - (i + 1), leftn)

    make("", 0, n)
    braket_li = list(set(braket_li))
    return braket_li


"""
print(make_braket(3))
"""


class Node:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right


def linked_list_sum(ln1, ln2):
    result_node = Node(0)

    def add_node(ln1, ln2, r_node, incent):
        if not (ln1 or ln2):
            if incent == 0:
                return
            else:
                r_node.right = Node(incent)
                return
        if not ln1:
            ln1 = Node(0)
        if not ln2:
            ln2 = Node(0)
        next_incent, ln_val = divmod(ln1.val + ln2.val + incent, 10)
        r_node.right = Node(ln_val)
        add_node(ln1.right, ln2.right, r_node.right, next_incent)

    add_node(ln1, ln2, result_node, 0)
    return result_node.right


"""
    ln1, ln1.right, ln1.right.right = Node(2), Node(4), Node(3)
    ln2, ln2.right, ln2.right.right = Node(5), Node(6), Node(4)
    result = linked_list_sum(ln1, ln2)
    print(result.val, result.right.val, result.right.right.val, result.right.right.right)
"""


class Node:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def tree_min_length(ln):
    num_li = []

    def get_num(ln):
        if ln:
            num_li.append(ln.val)
        else:
            return
        get_num(ln.left)
        get_num(ln.right)

    get_num(ln)
    num_li.sort()
    min_length = num_li[1] - num_li[0]
    for i in range(1, len(num_li) - 1):
        min_length = min([min_length, num_li[i + 1] - num_li[i]])
    print(min_length)


"""
    ln, ln.right = Node(4), Node(6)
    ln.left, ln.left.left, ln.left.right = Node(2), Node(1), Node(3)
    tree_min_length(ln)
"""


def make_set(nums):
    # output_li = []
    # def make_sun(add_nums, idx, left):
    #     if left==0:
    #     output_li.append(add_nums)
    #         return
    #     for i in range(idx, len(nums)):
    #         make_sun(add_nums+[nums[i]], i+1, left-1)

    # for i in range(len(nums)+1):
    #     make_sun([], 0, 1)
    # return output_li

    output_li = []

    def make_sun(add_nums, idx):
        output_li.append(add_nums)
        for i in range(idx, len(nums)):
            make_sun(add_nums + [nums[i]], i + 1)

    make_sun([], 0)
    return output_li
    """
    result = make_set([1, 2, 3])
    print(result)
    """


def find_route(m, n):
    # num = []
    # def find(curm, curn):
    #     if curm==m or curn==n:
    #         num.append('')
    #         return
    #     find(curm+1, curn)
    #     find(curm, curn+1)

    # find(1, 1)
    # return len(num)
    def dfs(m, n):
        if m == 0 or n == 0:
            return 1
        return dfs(m - 1, n) + dfs(m, n - 1)

    return dfs(m - 1, n - 1)

    """
    result = find_route(3, 2)
    print(result)
    """


def find_valid(s):
    opened = 0
    num = 0
    for i in s:
        if i == "(":
            opened += 1
        elif i == ")" and opened > 0:
            num += 2
            opened -= 1
    return num
    """
    result = find_valid(')(()())')
    print(result)
    """


def smile():
    print("^^")


def deco(func):
    def df():
        print("smile")
        func()
        print("smile end")

    return df


"""
# smile()
    smile = deco(smile)
    smile()
"""


def adder_deco(func):
    def ad(*args):
        print(*args, sep="+", end="")
        print(f"={func(*args)}")

    return ad


@adder_deco
def adder2(n1, n2):
    return n1 + n2


"""
adder2(3,4)
"""


def jump_game2(nums):
    import copy

    min_time = []

    def jump(idx, time):
        if idx >= len(nums) - 1:
            min_time.append(time)
            return
        length = nums[idx]
        for i in range(1, length + 1):
            jump(idx + i, time + 1)

    jump(0, 0)
    return min(min_time)


"""
    print(jump_game2([2,3,1,1,4]))
"""


def up_stairs(num):
    way = []

    def go_up(cur):
        if sum(cur) > num:
            return
        elif sum(cur) == num:
            way.append(cur)
            return
        go_up(cur + [1])
        go_up(cur + [2])

    go_up([])
    print(way, len(way))


"""
    up_stairs(2)
    up_stairs(3)
"""


def zigzag(s, numRows):
    row = [[] for i in range(numRows)]
    row_num = 0
    len_s = 0
    plus_minus = 1
    while True:
        if len_s == len(s):
            break
        if row_num == numRows - 1:
            plus_minus = -1
        elif row_num == 0:
            plus_minus = 1

        row[row_num].append(s[len_s])
        row_num += plus_minus
        len_s += 1
    return_word = ""
    for i in row:
        return_word += "".join(i)
    return return_word


"""
print(zigzag('PAYPALISHIRING', 4))
"""


def same_element_set(n1, n2):
    out_put_li = []
    for i in n1:
        if i in n2 and i not in out_put_li:
            out_put_li.append(i)
    return out_put_li


# 이진트리 bisect를 import하여 이용해볼 수 있다.
"""
print(same_element_set([1,2,2,1], [2,2]))
"""


def color_sort(n):
    import bisect

    result = []
    for i in n:
        result.insert(bisect.bisect_left(result, i), i)
    return result


"""
print(color_sort([2,0,2,1,1,0]))
"""


def fibonachi(n):
    def add(n):
        if n <= 1:
            return n
        return add(n - 1) + add(n - 2)

    print(add(n))
    """
    fibonachi(int(input()))
    """


def find_word(board, word):
    result = [False]

    def check_next_str(row_num, idx, left_word):
        if len(left_word) == 0:
            result.append(True)
            return
        if (
            row_num > len(board) - 1
            or row_num < 0
            or idx > len(board[0]) - 1
            or idx < 0
        ):
            return

        if board[row_num][idx] == left_word[0]:
            check_next_str(row_num + 1, idx, left_word[1:])
            check_next_str(row_num - 1, idx, left_word[1:])
            check_next_str(row_num, idx + 1, left_word[1:])
            check_next_str(row_num, idx - 1, left_word[1:])

    for row_num in range(len(board)):
        if word[0] in board[row_num]:
            idx = board[row_num].index(word[0])
            check_next_str(row_num, idx, word)
    return result[-1]


"""
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(find_word(board, word))
"""


def max_hystogram(heights):
    max_s = max(heights)
    for i in range(2, len(heights) + 1):
        for j in range(len(heights)):
            if i + j > len(heights):
                break
            box = heights[j : j + i]
            max_s = max([max_s, min(box) * i])
    return max_s


"""
    heights = [2, 1, 1, 6, 2, 3]
    # heights = [2, 4]
    print(max_hystogram(heights))
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def list_to_tree(nums):
    li_len = len(nums)
    node = Node(nums[li_len // 2])

    def add_node(node, nums, dir):
        li_len = len(nums)
        if li_len == 0:
            return
        if dir == "left":
            node.left = Node(nums[li_len // 2])
        if dir == "right":
            node.right = Node(nums[li_len // 2])
        add_node(node, nums[: li_len // 2], "left")
        add_node(node, nums[li_len // 2 :], "right")

    add_node(node, nums[: li_len // 2], "left")
    add_node(node, nums[li_len // 2 :], "right")
    return node


"""
    node = list_to_tree([-10, -3, 0, 5, 9])
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def list_to_tree(nums):
    li_len = len(nums)
    node = Node(nums[li_len // 2])
    print(node.val)

    def add_node(node, nums, dir):
        li_len = len(nums)
        if li_len == 0:
            return
        if dir == "left":
            node.left = Node(nums[li_len // 2])
            add_node(node.left, nums[: li_len // 2 - 1], "left")
            add_node(node.left, nums[li_len // 2 + 1 :], "right")
            print(node.left.val)
        if dir == "right":
            node.right = Node(nums[li_len // 2])
            print(node.right.val)
            add_node(node.right, nums[: li_len // 2 - 1], "left")
            add_node(node.right, nums[li_len // 2 + 1 :], "right")

    add_node(node, nums[: li_len // 2], "left")
    add_node(node, nums[li_len // 2 :], "right")
    return node
    """
    node = list_to_tree([-10, -3, 0, 5, 9])
    print(node.val, node.left.val, node.left.left, node.left.right)
    print(node.right.val, node.right.right, node.right.left)
    """


def buy_sell(prices):
    money_sum = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            money_sum += prices[i + 1] - prices[i]
    return money_sum
    """
    print(buy_sell([7,1,5,3,6,4]))
    print(buy_sell([1,2,3,4,5]))
    """


def word_puzzle(s, word_Dict):
    result = [False]

    def erase_s(left_s):
        if left_s == "":
            result.append(True)
            return
        for i in word_Dict:
            split_word = left_s.split(i, maxsplit=1)
            if split_word[0] == "":
                erase_s(split_word[1])

    erase_s(s)
    return result[-1]


"""
    s = 'leetcode'
    word_Dict = ["leet", "code"]
    print(word_puzzle(s, word_Dict))
    
    s = 'applepenapple'
    word_Dict = ["apple", "pen"]
    print(word_puzzle(s, word_Dict))
    
    s = 'catsandog'
    word_Dict = ["cats", "dog", "sand", "and", "cat"]
    print(word_puzzle(s, word_Dict))
"""


def middle_node(ln):
    node_li = []

    def preorder(ln):
        if ln == None:
            return
        preorder(ln.left)
        node_li.append(ln.val)
        preorder(ln.right)

    preorder(ln)
    return node_li


"""
    ln, ln.right, ln.right.left = Node(1), Node(2), Node(3)
    print(middle_node(ln))
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def linked_li_move(ln, x):
    re_ln = Node(0)
    big = []
    a = re_ln
    while ln:
        if ln.val < x:
            a.right = Node(ln.val)
            a = a.right
        else:
            big.append(ln.val)
        ln = ln.right
    while big:
        a.right = Node(big.pop(0))
        a = a.right
    return re_ln.right


"""
    ln, ln.right, ln.right.right = Node(1), Node(4), Node(3)
    ln.right.right.right, ln.right.right.right.right = Node(2), Node(5)
    ln.right.right.right.right.right = Node(2)
    b = linked_li_move(ln, 3)
    while b:
        print(b.val)
        b = b.right
"""


def small_height_root(n, edges):
    from collections import defaultdict

    root_dic = defaultdict(list)
    for i, j in edges:
        root_dic[i].append(j)
        root_dic[j].append(i)
    while len(root_dic) > 2:
        del_li = []
        for i, j in root_dic.items():
            if len(j) == 1:
                root_dic[j[0]].remove(i)
                del_li.append(i)
        for i in del_li:
            root_dic.pop(i)
    return [i for i in root_dic.keys()]


"""
    n = 6
    edges = [[3, 0], [3,1], [3,2], [3,4], [5,4]]
    print(small_height_root(n, edges))
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def valid_tree(ln):
    result = [True]

    def order(ln):
        if ln == None:
            return None
        left = order(ln.left)
        right = order(ln.right)
        cur = ln.val
        if left == None:
            left = cur - 1
        if right == None:
            right = cur + 1
        if cur > left and cur < right:
            pass
        else:
            result.append(False)
        return cur

    order(ln)
    return result[-1]


"""
    ln, ln.left, ln.right = Node(5), Node(1), Node(4)
    ln.right.left, ln.right.right = Node(3), Node(6)
    print(valid_tree(ln))
"""


def linked_nums(nums):
    nums = sorted(list(set(nums)))
    max_time = 0
    for i in range(len(nums)):
        cur_num = nums[i]
        time = 1
        while True:
            cur_num += 1
            if cur_num in nums:
                time += 1
            else:
                max_time = max(time, max_time)
                break
    return max_time


"""
nums = [100, 4, 200, 1, 3, 2]
# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(linked_nums(nums))
"""

# call by reference (assignment)
# call by value


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def tree_to_llist(ln):
    def order(ln):
        if not ln:
            return
        cur = ln.val
        order(ln.left)
        order(ln.right)
        if ln.right:
            if ln.left:
                leftn = ln.left
                while True:
                    if leftn.left:
                        leftn = leftn.left
                    else:
                        break
                leftn.left = ln.right
                ln.right = None
            else:
                ln.left = ln.right
                ln.right = None

    order(ln)
    """
    ln, ln.left, ln.left.left, ln.left.right = Node(1), Node(2), Node(3), Node(4)
    ln.right, ln.right.right = Node(5), Node(6)
    tree_to_llist(ln)
    while ln:
        print(ln.val)
        if ln.right:
            print(ln.right.val, "right")
        ln = ln.left
    """


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)


"""
minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def twobinaryTreeRight(ln):
    import copy

    result_li = []
    que = [ln]
    while que:
        result_li.append(que[-1].val)
        lastq = copy.deepcopy(que)
        que = []
        for last in lastq:
            if last.left:
                que.append(last.left)
            if last.right:
                que.append(last.right)
    print(result_li)


"""
ln, ln.left, ln.left.right = Node(1), Node(2), Node(5)
ln.right, ln.right.right = Node(3), Node(4)
twobinaryTreeRight(ln)
"""

# 이진 탐색 트리의 범위 합
def sum_tree(ln, low, high):
    sum_li = []

    def go_down(ln):
        if ln == None:
            return
        else:
            if low <= ln.val <= high:
                sum_li.append(ln.val)
        go_down(ln.left)
        go_down(ln.right)

    go_down(ln)
    return sum(sum_li)


"""
    ln, ln.left, ln.left.left, ln.left.right = Node(10), Node(5), Node(3), Node(7)
    ln.right, ln.right.right = Node(15), Node(18)
    print(sum_tree(ln, 7, 15))
"""

# 합이 가장 큰 연속적인 하위 배열
def linked_sum_big(li):
    sum_num = 0
    new_li = []
    num = False
    num_plus = 0
    for i in li:
        if i > 0:
            num_check = True
        else:
            num_check = False
        if num == num_check:
            num_plus += i
        else:
            new_li.append(num_plus)
            num_plus = i
        num = num_check
    new_li.append(num_plus)
    if len(new_li) == 1:
        if new_li[0] >= 0:
            return new_li[0]
        else:
            return max(li)
    new_li.append(0)
    sum_li = []
    for i in range(len(new_li)):
        if new_li[i] < 0:
            if new_li[i] + new_li[i + 1] >= 0:
                sum_num += new_li[i]
            else:
                sum_li.append(sum_num)
                sum_num = 0
        else:
            sum_num += new_li[i]
        if sum_num < 0:
            sum_num = 0
    sum_li.append(sum_num)
    return sum(sum_li)
    """
    # li = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 100]
    li = [-3, -2, 5, -6, -8]
    print(linked_sum_big(li))
    """


# 슬라이딩 윈도우
def sliding_window(nums, k):
    output = []
    for i in range(len(nums) + 1 - k):
        j = i + k
        li = nums[i:j]
        output.append(max(li))
    return output


"""
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(sliding_window(nums, k))
"""

# 2개의 중복되는 숫자 찾기
def two_same_num(nums):
    while nums:
        num = nums.pop()
        if num in nums:
            return num


"""
    nums = [1,3,4,2,2]
    print(two_same_num(nums))
    nums = [3,1,3,4,2]
    print(two_same_num(nums))
"""


def add_same_list(lists):
    lists.sort()
    result_li = []
    while lists:
        last_li = lists.pop()
        if lists:
            secl_li = lists.pop()
        else:
            result_li = [last_li] + result_li
            break
        if last_li[0] <= secl_li[1]:
            lists.append([secl_li[0], last_li[1]])
        else:
            result_li = [last_li] + result_li
            lists.append(secl_li)
    return result_li


"""
    lists = [[1,3], [2,6], [6,10], [15,18]]
    print(add_same_list(lists))
    print(lists)
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def tree_line_sum(ln):
    sum_list = []

    def last_mid(ln):
        if not ln:
            return 0
        left_val = max(last_mid(ln.left), 0)
        right_val = max(last_mid(ln.right), 0)
        cur_val = ln.val
        sum_list.append(left_val + right_val + cur_val)
        return max([left_val + cur_val, right_val + cur_val])

    last_mid(ln)
    return max(sum_list)


if __name__ == "__main__":
    ln, ln.left, ln.right = Node(-10), Node(9), Node(20)
    ln.right.left, ln.right.right = Node(15), Node(7)
    print(tree_line_sum(ln))
