n = int(input())
arr = list(map(int, input().split()))
sorted_arr = []

index = 0
sorted_arr.append(arr[0])
while (index <= n):

    sorted_arr.sort()
    print(sorted_arr[index // 2], end=' ')
    index += 2
    if index < n:
        sorted_arr.append(arr[index - 1])
        sorted_arr.append(arr[index])
    else:
        break

