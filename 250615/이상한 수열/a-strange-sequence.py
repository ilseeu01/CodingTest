n = int(input())
arr = [0 for _ in range(n)]
arr[0] = 1
arr[1] = 2

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2


    return solution(n//3) + solution(n-1)

print(solution(n))