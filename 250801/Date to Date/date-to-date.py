
m1, d1, m2, d2 = map(int, input().split())

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

elapsed_days = 1
for i in range(m1, m2):
    elapsed_days += num_of_days[i]

elapsed_days += (d2 - d1)

print(elapsed_days)
