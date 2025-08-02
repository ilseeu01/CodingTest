n = input()
length = len(n) - 1

digits = 0
for digit in n:
    digit = int(digit)
    digits += digit * (2 ** length)
    length -= 1

digits *= 17
res = []

while True:
    if digits < 2:
        res.append(digits)
        break
    res.append(digits % 2)
    digits //= 2

for digit in res[::-1]:
    print(digit, end="")