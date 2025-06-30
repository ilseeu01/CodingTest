import string
n, k, t = input().split()
n = int(n)
k = int(k)

arr = [input().strip() for _ in range(n)]

# 문자열 클린 함수: 제어 문자 제거
def is_clean(s):
    return all(ch in string.printable and ch not in string.whitespace[1:] for ch in s)

# 클린 + 필터링
filtered_arr = []

for word in arr:
    if not is_clean(word):
        continue  # 이상한 문자 하나라도 있으면 스킵
    if t in word:
        filtered_arr.append(word)

filtered_arr.sort()
print(filtered_arr[k-1])

