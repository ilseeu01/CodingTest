class Student:
    def __init__(self, name, kor, mat, eng):
        self.name = name
        self.kor = kor
        self.mat = mat
        self.eng = eng

n = int(input())
student = [Student(*input().split()) for _ in range(n)]
for s in student:
    s.kor = int(s.kor)
    s.mat = int(s.mat)
    s.eng = int(s.eng)
sorted_student = sorted(student, key=lambda x: x.kor+x.mat+x.eng)

for s in sorted_student:
    print(f"{s.name} {s.kor} {s.mat} {s.eng}")
