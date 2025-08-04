n = int(input())
arr = [0] * (2001)
start = 1000

for _ in range(n):
    x, move = input().split()
    

    if move == "R":
        x = int(x) + start
        for i in range(start, x):
            arr[i] += 1
        start = x
    elif move == "L":
        x = start - int(x)
        for i in range(x, start):
            arr[i] += 1
        start = x


count = 0
for i in range(2001):
    if arr[i] >= 2:
        count += 1
    
print(count)
