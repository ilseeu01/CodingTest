class Set:
    def __init__(self, id, level):
        self.id = id
        self.level = level

set1 = Set("codetree", 10)
id, level = input().split()
set2 = Set(id, level)

print(f"user {set1.id} lv {set1.level}")
print(f"user {set2.id} lv {set2.level}")