n = int(input()) * 2
arr = list(map(int, input().split()))

arr.sort()

max = 0
for i in range(n//2):
    if max < arr[i] + arr[n-1-i]:
        max = arr[i] + arr[n-1-i]


#max = arr[n//2] + arr[n//2 + 1]
#print(arr)
print(max)

