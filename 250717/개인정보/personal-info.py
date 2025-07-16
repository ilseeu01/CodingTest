class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = [Person(*input().split()) for _ in range(5)]
for p in people:
    p.height = int(p.height)
    p.weight = float(p.weight)

people_by_name = sorted(people, key=lambda x: x.name)
people_by_height = sorted(people, key=lambda x: -x.height)

print("name")
for p in people_by_name:
    print(f"{p.name} {p.height} {p.weight:.1f}")

print()
print("height")
for p in people_by_height:
    print(f"{p.name} {p.height} {p.weight:.1f}")
