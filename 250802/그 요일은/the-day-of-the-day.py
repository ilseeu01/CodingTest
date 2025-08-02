m1, d1, m2, d2 = map(int, input().split())
day = input()

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 첫 날짜 절대일수
elapsed_days1 = sum(num_of_days[:m1]) + d1
# 두 번째 날짜 절대일수
elapsed_days2 = sum(num_of_days[:m2]) + d2

delta = elapsed_days2 - elapsed_days1

# 기준 요일 인덱스
idx = days.index(day)

# 기준 날짜(첫날) 요일 (1월 1일이 Mon이라고 가정)
start_day = (elapsed_days1 % 7)  # 1월 1일이 Mon이므로 0이 Mon
target_day = idx

# 첫날부터 두번째날까지 타겟 요일 계산
cnt = delta // 7
if (start_day + delta % 7) >= target_day + (0 if start_day <= target_day else 7):
    cnt += 1

print(cnt)
