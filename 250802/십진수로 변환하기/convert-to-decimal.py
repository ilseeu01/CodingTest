n = input()
length = len(n) - 1

digits = 0
for digit in n:
    digit = int(digit)
    digits += digit * (2 ** length)
    length -= 1

print(digits)