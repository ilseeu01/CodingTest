a, b = map(int, input().split())
n = input()
length = len(n) - 1

digits = 0
for digit in n:
    digit = int(digit)
    digits += digit * (a ** length)
    length -= 1

n = int(digits)

digits = []

while True:
    if n < b:
        digits.append(n)
        break
    digits.append(n % b)
    n //= b

for digit in digits[::-1]:
    print(digit, end="")