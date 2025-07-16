class Number:
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx

n = int(input())
values = list(map(int, input().split()))
number = []
for idx, value in enumerate(values):
    number.append(Number(value, idx+1))

sorted_number = sorted(number, key=lambda x: x.value)

for s in sorted_number:
    print(f"{s.idx}", end=" ")