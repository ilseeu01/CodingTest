n = int(input())
arr = list(map(int, input().split()))

# 최댓값 찾기
max_num = arr[0]

for i in range(1, n):
    if arr[i] > max_num:
        max_num = arr[i]

# 최댓값의 자릿수 구하기
digit_num = 0

while max_num > 0:
    max_num //= 10
    digit_num += 1

# 일의 자리 → 십의 자리 → 백의 자리 ...
for pos in range(digit_num):

    # 0~9 버킷 생성
    buckets = [[] for _ in range(10)]

    # 현재 자릿수를 기준으로 버킷에 넣기
    for num in arr:
        digit = (num // (10 ** pos)) % 10
        buckets[digit].append(num)

    # 버킷을 0 → 9 순서로 다시 arr에 합치기
    arr = []

    for bucket in buckets:
        for num in bucket:
            arr.append(num)

print(*arr)