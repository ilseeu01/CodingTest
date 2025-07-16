class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())
student = []

for idx in range(n):
    height, weight = map(int, input().split())
    student.append(Student(height, weight, idx+1))

sorted_student = sorted(student, key=lambda x: (-x.height, -x.weight, x.number))

for s in sorted_student:
    print(f"{s.height} {s.weight} {s.number}")