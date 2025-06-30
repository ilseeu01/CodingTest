n, k, t = input().split()
n = int(n)
k = int(k)

arr = [input().strip() for _ in range(n)]

sorted_arr = []
for i in range(n):
    if t in arr[i]:
        sorted_arr.append(arr[i])

arr.sort()
print(arr[k])