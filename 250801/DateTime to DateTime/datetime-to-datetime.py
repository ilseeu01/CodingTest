import sys

a, b, c = map(int, input().split())

if a <= 11 and (b < 11 or c < 11):
    print(-1)
    sys.exit(0)

elasped_min = (a - 11) * 24 * 60 + (b - 11) * 60 + (c - 11)
print(elasped_min)

