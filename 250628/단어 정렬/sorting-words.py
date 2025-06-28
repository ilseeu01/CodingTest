n = int(input())
arr = [input() for _ in range(n)]  # 문자열 n줄 입력받아 리스트로 저장


arr.sort()
print('\n'.join(arr))