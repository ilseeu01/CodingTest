n = int(input())
arr = list(map(int, input().split()))

index = 1
while (index <= n):
    if index % 2 == 1:
        arr.sort()
        print(arr[index // 2], end=' ')
        index += 2

