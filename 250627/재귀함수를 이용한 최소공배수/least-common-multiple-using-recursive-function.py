n = int(input())
arr = list(map(int, input().split()))

def get_gcd(a, b):
    if b == 0:
        return a
    tmp = a % b
    return get_gcd(b, tmp)

def get_lcm(a, b):   
    return (a * b) // get_gcd(a, b)


lcm = arr[0]

for i in range(1, n):
    lcm = get_lcm(lcm, arr[i])
  
print(lcm)