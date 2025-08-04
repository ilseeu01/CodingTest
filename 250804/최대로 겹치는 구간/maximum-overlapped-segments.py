n = int(input())
x1, x2 = map(int, input().split())

x1 += 100
x2 += 100

arr = [0 for _ in range(201)]

for _ in range(n):
    for i in range(x1, x2):
        arr[i] += 1

print(max(arr))
