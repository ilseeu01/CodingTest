n, b = map(int, input().split())
digits = []

def dex2bin(n):
    while True:
        if n < 2:
            digits.append(n)
            break
        digits.append(n % 2)
        n //= 2

    for digit in digits[::-1]:
        print(digit, end="")

def dex2qua(n):
    while True:
        if n < 4:
            digits.append(n)
            break
        digits.append(n % 4)
        n //= 4

    for digit in digits[::-1]:
        print(digit, end="")

def dex2oct(n):
    while True:
        if n < 8:
            digits.append(n)
            break
        digits.append(n % 8)
        n //= 8

    for digit in digits[::-1]:
        print(digit, end="")

if b == 2:
    dex2bin(n)
elif b == 4:
    dex2qua(n)
elif b == 8:
    dex2oct(n)