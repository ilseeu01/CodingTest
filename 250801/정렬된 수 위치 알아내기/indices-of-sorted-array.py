class Number:
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx

n = int(input())
values = list(map(int, input().split()))
number = []
position = [0 for _ in range(n)]

for idx, value in enumerate(values):
    number.append(Number(value, idx))

#sorted_number = sorted([Number(num.value, num.idx) for num in number], key=lambda x: (x.value, x.idx))
number.sort(key=lambda x: (x.value, x.idx))
for idx, num in enumerate(number):
    position[num.idx] = idx + 1

print(*position)