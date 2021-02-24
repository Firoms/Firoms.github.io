class student:
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department
        self.majorscore = {}
        self.gpa = 0

    def score_init(self, score_dict):
        self.majorscore = score_dict
        for _, key in self.majorscore.items():
            self.gpa += key
        self.gpa = self.gpa / len(self.majorscore)

    def get_gpa(self):
        print(self.gpa)


class School:
    def __init__(self):
        self.departdict = {}

    def new_student(self, one_student):

        if type(one_student) == list:
            for i in one_student:
                if i.department in self.departdict.keys():
                    self.departdict[i.department].append(i)
                else:
                    self.departdict[i.department] = [i]
        else:
            if one_student.department in self.departdict.keys():
                self.departdict[one_student.department].append(one_student)
            else:
                self.departdict[one_student.department] = [one_student]
        print(self.departdict)

    def scholarship(self):
        for studentlist in self.departdict.values():
            for single_student in studentlist:
                max_gpa = 0
                if max_gpa < single_student.gpa:
                    best_dep = single_student.department
                    best_nam = single_student.name
                    max_gpa = single_student.gpa
                else:
                    pass
            print(best_dep, end=" ")
            print(best_nam)


class Lecture:
    def __init__(self, name, prof, student_list):
        self.lecturename = name
        self.prof = prof
        self.name = name
        self.student = student_list

    def best_student(self):
        max_score = 0

        for single_student in self.student:
            if self.lecturename in single_student.majorscore.keys():
                if max_score < single_student.majorscore[self.name]:
                    max_score = single_student.majorscore[self.name]
        print(f"{self.name}의 수석 학생은", end="")
        for single_student in self.student:
            if self.lecturename in single_student.majorscore.keys():
                if max_score == single_student.majorscore[self.name]:
                    best = single_student.name
                    print(f" {best}({max_score}) ", end="")
        print("입니다.")


# student 객체 생성
student1 = student("2018311658", "차민지", "데이터사이언스융합전공")
student2 = student("2018311123", "이하은", "데이터사이언스융합전공")
student3 = student("1234567890", "오혜준", "기계공학과")
student4 = student("1234123232", "김경수", "기계공학과")
student5 = student("1232165466", "양승진", "기계공학과")
student6 = student("2018311897", "김민수", "바이오메카트로닉스")

# school 객체 생성 및 학생들 입력
# ex) school.new_student(student1)

# Your code
school1 = School()
school1.new_student(student1)
school1.new_student([student2, student3, student4, student5])
school1.new_student([student6])


# 학생별 성적 입력
# 차민지
student1.score_init({"미분적분학1": 2.5, "확률과통계": 4.5, "이산수학": 3.5})
print(student1.gpa)
# 이하은
student2.score_init({"미분적분학1": 4.5, "확률과통계": 4.0, "이산수학": 4.5, "미분적분학2": 4.5})
print(student2.gpa)
# 오혜준
student3.score_init({"미분적분학1": 3.0, "확률과통계": 4.0, "일반화학1": 4.0})

# 김경수
student4.score_init({"미분적분학1": 3.5, "확률과통계": 4.2, "일반화학2": 2.5})

# 양승진
student5.score_init({"미분적분학1": 3.5, "일반물리1": 3.9, "일반화학2": 3.0})

# 김민수
student6.score_init({"미분적분학1": 3.5, "일반물리1": 3.6, "일반화학2": 3.0, "미분적분학2": 4.2})

# 학과별 성적이 제일 높은 학생 출력(코딩 완료 후 주석 해제)
# school.scholarship()
school1.scholarship()

# 과목별로 best student 출력
# ex) chem1.best_student()

# Your Code
student_list = [student1, student2, student3, student4, student5, student6]
cal1_student = []
cal2_student = []
prob_student = []
disc_student = []
phy1_student = []
chem1_student = []
chem2_student = []


for single_student in student_list:
    if "미분적분학1" in single_student.majorscore.keys():
        cal1_student.append(single_student)
    if "미분적분학2" in single_student.majorscore.keys():
        cal2_student.append(single_student)
    if "확률과통계" in single_student.majorscore.keys():
        prob_student.append(single_student)
    if "이산수학" in single_student.majorscore.keys():
        disc_student.append(single_student)
    if "일반물리1" in single_student.majorscore.keys():
        phy1_student.append(single_student)
    if "일반화학1" in single_student.majorscore.keys():
        chem1_student.append(single_student)
    if "일반화학2" in single_student.majorscore.keys():
        chem2_student.append(single_student)

cal1 = Lecture("미분적분학1", "이혜경", cal1_student)
cal1.best_student()
cal2 = Lecture("미분적분학2", "루이스사이몬", cal2_student)
cal2.best_student()
prob = Lecture("확률과통계", "길이만", prob_student)
prob.best_student()
disc = Lecture("이산수학", "설한국", disc_student)
disc.best_student()
phy1 = Lecture("일반물리1", "랍라하예", phy1_student)
phy1.best_student()
chem1 = Lecture("일반화학1", "이진용", chem1_student)
chem1.best_student()
chem2 = Lecture("일반화학2", "부진효", chem2_student)
chem2.best_student()
