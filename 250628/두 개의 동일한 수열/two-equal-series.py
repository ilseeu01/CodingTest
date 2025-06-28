n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

def check(arr1, arr2, n):
    for i in range(n):
        if arr1[i] != arr2[i]:
            print("No")
            return
    print("Yes")

check(arr1, arr2, n)