import random
from datetime import datetime

# cmd pip , pip list, pip install virtualenv
# virtualenv 파일명 , cd 파일명, dir, cd Scripts, activate.bat
# 탭탭 자동완성  //// 가상환경에 넣을  파일 찾아가기
# 시스템 속성 path
# test >> assert
class User:
    def __init__(self):
        self.name = input("유저 이름을 말해주세요\n")


# 숫자뽑기
def ran_pick():
    ran_nums = random.sample(range(1, 46), 7)
    return ran_nums


# 검증 1 - 숫자 개수 확인
def test_num_len(ran_nums):
    if len(ran_nums) == 7:
        print("숫자가 7개 맞습니다.")
        return True
    else:
        print("숫자가 7개 아닙니다.")
        return False


# 검증 2 - 숫자 범위 확인
def test_num_range(ran_nums):
    for i in range(0, 7):
        if ran_nums[i] in range(1, 46):
            pass
        else:
            print("숫자 중 범위에 맞지 않는 숫자가 있습니다.")
            return False
    print("모든 숫자가 범위안에 들어갑니다.")
    return True


# 검증 3 - 숫자 중복 확인
def test_num_dif(ran_nums):
    for i in range(0, 7):
        if ran_nums[i] in ran_nums[i + 1 :]:
            print("중복된 숫자가 있습니다.")
            return False
        else:
            pass
    print("중복된 숫자가 없습니다.")
    return True


# 숫자 생성(검증 포함)
def generate():
    while True:
        lotto_nums = ran_pick()
        print(lotto_nums)
        print("////////////")
        if (
            test_num_len(lotto_nums)
            and test_num_range(lotto_nums)
            and test_num_dif(lotto_nums)
        ):
            print("숫자 체크 완료했습니다")
            return lotto_nums
        print("다시 숫자를 뽑습니다.\n")


# 로또 숫자 세이브
def num_save():
    print(lotto_nums)
    f = open(f"{User1.name} 로또번호저장.txt", "a")
    cnt = 0
    f.write(datetime.today().strftime("%Y%m%d"))
    for i in lotto_nums:
        cnt += 1
        f.write(f",{i}")
    f.write("\n")
    f.close()


# 사용자 별 날짜 중복 확인
def User_date_check():
    try:
        f = open(f"{User1.name} 로또번호저장.txt", "r")
        last_num = f.readlines()[-1]
        last_date = last_num.split(",")[0]
        f.close()
        if last_date == datetime.today().strftime("%Y%m%d"):
            print("오늘 이미 로또를 뽑으셨습니다. ")
        else:
            num_save()
    except:
        print(f"{User1.name}님은 번호를 처음 뽑으시는 분입니다.")
        num_save()


if __name__ == "__main__":
    lotto_nums = []
    User1 = User()
    print(User1.name)
    lotto_nums = generate()
    User_date_check()
