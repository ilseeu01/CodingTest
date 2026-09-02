n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
sorted = True
while sorted == True:
    sorted = False
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            sorted = True

print(*arr)