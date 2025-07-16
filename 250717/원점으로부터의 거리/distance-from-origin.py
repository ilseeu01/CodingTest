class Point:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num


n = int(input())
point = []
for idx in range(n):
    x, y = map(int, input().split())
    point.append(Point(x,y,idx+1))

sorted_point = sorted(point, key=lambda x: abs(x.x) + abs(x.y))
for p in sorted_point:
    print(f"{p.num}")
