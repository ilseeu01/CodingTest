m1, d1, m2, d2 = map(int, input().split())
day = input()
#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#days = [" ", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]



elapsed_days1 = 0
for i in range(m1):
    elapsed_days1 += num_of_days[i]

elapsed_days1 += d1
day1 = elapsed_days1 % 7 #이게 월요일

elapsed_days2 = 0
for i in range(m2):
    elapsed_days2 += num_of_days[i]

elapsed_days2 += d2
day2 = elapsed_days2 % 7

res = (elapsed_days2 - elapsed_days1) % 7

for i in range(6):
    if day == days[i]:
        idx = i

if res < idx:
    res -= 1
print(res)