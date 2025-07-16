class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
people = [Person(*input().split()) for _ in range(n)]
for p in people:
    p.height = int(p.height)
    p.weight = int(p.weight)

sorted_people = sorted(people, key=lambda x: (x.height, -x.weight))
for p in sorted_people:
    print(f"{p.name} {p.height} {p.weight}")