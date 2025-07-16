class Student:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

n = int(input())
student = [Student(*input().split()) for _ in range(n)]

for score in student:
    score.kor = int(score.kor)
    score.eng = int(score.eng)
    score.mat = int(score.mat)

sorted_student = sorted(student, key=lambda x: (-x.kor, -x.eng, -x.mat))

for s in sorted_student:
    print(f"{s.name} {s.kor} {s.eng} {s.mat}")