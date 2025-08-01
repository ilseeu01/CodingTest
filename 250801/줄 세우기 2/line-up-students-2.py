class Student:
    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx

n = int(input())
student = [Student(*input().split()) for _ in range(n)]
for stu in student:
    stu.height = int(stu.height)
    stu.weight = int(stu.weight)

student.sort(key=lambda x: (x.height, -x.weight))

for idx, value in enumerate(student):
    print(f"{value.height} {value.weight} {idx+1}")