class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
people = [Person(*input().split()) for _ in range(n)]
for p in people:
    p.height = int(p.height)

sorted_person = sorted(people, key=lambda x: x.height)
for line in sorted_person:
    print(f"{line.name} {line.height} {line.weight}")